# checkout/webhook_handler.py

import json
import time
import logging
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from profiles.models import UserProfile
import stripe

# Setting up logging to track events and errors in the webhook handler
logger = logging.getLogger(__name__)

class StripeWH_Handler:
    """Handles Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Sends a confirmation email to the user after an order is successfully processed"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )
            logger.info(f"Confirmation email sent to {cust_email}")
        except Exception as e:
            logger.error(f"Error sending email: {e}")

    def handle_event(self, event):
        """
        Handles a generic/unknown/unexpected webhook event from Stripe.
        Logs the event and returns an HTTP 200 response.
        """
        logger.info(f"Received unknown webhook event: {event['type']}")
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handles the payment_intent.succeeded webhook from Stripe.
        Creates or verifies an order in the database based on Stripe data.
        """
        intent = event.data.object

        logger.info(f"Intent data: {json.dumps(intent, indent=2)}")

        pid = intent.id
        bag = getattr(intent.metadata, 'bag', None)  # Retrieving bag data from metadata
        save_info = getattr(intent.metadata, 'save_info', False)  # Retrieving save_info flag from metadata

        # Проверяем, существует ли поле charges
        if hasattr(intent, 'charges') and len(intent.charges.data) > 0:
            billing_details = intent.charges.data[0].billing_details
            grand_total = round(intent.charges.data[0].amount / 100, 2)
        elif hasattr(intent, 'payment_method'):
            # Используем данные из payment_method если charges отсутствуют
            payment_method_data = stripe.PaymentMethod.retrieve(intent.payment_method)
            billing_details = payment_method_data.billing_details
            grand_total = round(intent.amount / 100, 2)
        else:
            logger.error("No valid billing details found in intent")
            return HttpResponse(
                content=f"Webhook received: {event['type']} | ERROR: No billing details found",
                status=500
            )

        shipping_details = intent.shipping

        # Очищаем пустые поля в shipping_details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Обновляем профиль пользователя, если save_info отмечен
        profile = None
        username = getattr(intent.metadata, 'username', 'AnonymousUser')
        if username != 'AnonymousUser':
            try:
                profile = UserProfile.objects.get(user__username=username)
                if save_info:
                    profile.default_phone_number = shipping_details.phone
                    profile.default_country = shipping_details.address.country
                    profile.default_postcode = shipping_details.address.postal_code
                    profile.default_town_or_city = shipping_details.address.city
                    profile.default_street_address1 = shipping_details.address.line1
                    profile.default_street_address2 = shipping_details.address.line2
                    profile.default_county = shipping_details.address.state
                    profile.save()
                    logger.info(f"Profile updated for user {username}")
            except UserProfile.DoesNotExist:
                logger.error(f"User profile not found for {username}")

        # Проверяем, существует ли заказ в базе данных
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                logger.info(f"Order already exists: {order.id}")
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        # Если заказ существует, отправляем подтверждение по email
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            # Если заказ не существует, создаём новый
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                # Добавляем товары в заказ
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                logger.info(f"Order created successfully: {order.id}")
            except Exception as e:
                if order:
                    order.delete()  # Откатываем создание заказа, если что-то пошло не так
                logger.error(f"Error creating order: {e}")
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        
        # Отправляем подтверждение по email
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handles the payment_intent.payment_failed webhook from Stripe.
        Logs a warning that the payment failed.
        """
        logger.warning(f"Payment failed: {event['type']}")
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)