""" booking/webhook_handler.py """

import json
import logging
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from booking.models import Booking
import stripe

stripe.api_version = settings.STRIPE_API_VERSION 

logger = logging.getLogger(__name__)


class StripeWH_Handler:
    """Handles Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handles an unknown webhook event"""
        logger.info(f"Unknown webhook event: {event['type']}")
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handles payment success event"""
        intent = event.data.object
        session = event.data.object
        logger.info(f"Intent data: {json.dumps(intent, indent=2)}")
        
        booking_id = intent.metadata.get('booking_id')

        if not booking_id:
            logger.error("Booking ID missing in webhook metadata.")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: '
                        f'Booking ID missing',
                status=400)

        try:
            booking = Booking.objects.get(id=booking_id)
            booking.confirm_booking()
            logger.info(
                f"Booking {booking_id} confirmed and email sent."
            )
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: '
                        f'Booking confirmed',
                status=200)
        except Booking.DoesNotExist:
            logger.error(f"Booking with ID {booking_id} not found.")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: '
                        f'Booking not found',
                status=500)
        except Exception as e:
            logger.error(f"Error processing booking {booking_id}: {e}")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: {str(e)}',
                status=500)

    def handle_payment_intent_payment_failed(self, event):
        """Handles payment failure event"""
        logger.warning(f"Payment failed: {event['type']}")
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_checkout_session_completed(self, event):
        """Handles successful checkout session"""
        session = event.data.object
        logger.info(
            f"Checkout session completed: "
            f"{json.dumps(session, indent=2)}"
        )

        booking_id = session.client_reference_id

        try:
            booking = Booking.objects.get(id=booking_id)
            booking.confirm_booking()
            self._send_confirmation_email(booking)
            logger.info(
                f"Booking {booking_id} confirmed and email sent."
            )
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: '
                        f'Booking confirmed',
                status=200)
        except Booking.DoesNotExist:
            logger.error(f"Booking with ID {booking_id} not found.")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: '
                        f'Booking not found',
                status=500)

    def handle_checkout_session_async_payment_failed(self, event):
        """Handles async payment failure"""
        session = event.data.object
        logger.warning(
            f"Checkout session payment failed: "
            f"{json.dumps(session, indent=2)}"
        )

        booking_id = session.client_reference_id

        try:
            booking = Booking.objects.get(id=booking_id)
            booking.cancel_booking()
            logger.info(
                f"Booking {booking_id} cancelled due to payment failure."
            )
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: '
                        f'Booking cancelled',
                status=200)
        except Booking.DoesNotExist:
            logger.error(f"Booking with ID {booking_id} not found.")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: '
                        f'Booking not found',
                status=500)

    def _send_confirmation_email(self, booking):
        """Sends a confirmation email after booking"""
        profiles = booking.user.userprofile
        context = {'booking': booking, 'profiles': profiles}

        subject = f"Booking Confirmation - {booking.id}"
        email_html_message = render_to_string(
            'booking/booking_confirmation_email.html',
            context
        )
        recipient_email = profiles.user.email

        send_mail(
            subject,
            '',
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            fail_silently=False,
            html_message=email_html_message,
        )

        logger.info(f"Confirmation email sent to {recipient_email}")
