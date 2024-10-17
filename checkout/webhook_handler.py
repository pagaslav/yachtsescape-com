# checkout/webhook_handler.py

import json
import logging
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from booking.models import Booking
from django.utils.timezone import now
import stripe

stripe.api_version = settings.STRIPE_API_VERSION 

# Setting up logging to track events and errors in the webhook handler
logger = logging.getLogger(__name__)

class StripeWH_Handler:
    """Handles Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, booking):
        """Sends a confirmation email to the user after a booking is successfully processed"""
        cust_email = booking.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'booking': booking})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'booking': booking, 'contact_email': settings.DEFAULT_FROM_EMAIL})

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
        """Handles a generic/unknown/unexpected webhook event from Stripe."""
        logger.info(f"Received unknown webhook event: {event['type']}")
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handles the payment_intent.succeeded webhook from Stripe."""
        # intent = event.data.object
        session = event.data.object
        # logger.info(f"Intent data: {json.dumps(intent, indent=2)}")
        logger.info(f"Intent data: {json.dumps(session, indent=2)}")
        
        # Retrieve the booking ID from metadata
        booking_id = getattr(session, 'client_reference_id', None)
        # booking_id = intent.metadata.get('booking_id')
        # logger.error(f"Metadata received: {intent.metadata}")
        logger.error(f"Retrieved booking_id: {booking_id}")

        # Check if booking_id is None
        # if booking_id is None:
        #     logger.error("Booking ID is missing in the webhook metadata.")
        #     return HttpResponse(
        #         content=f'Webhook received: {event["type"]} | ERROR: Booking ID missing',
        #         status=400)

        try:
            # Fetch the booking associated with this payment
            booking = Booking.objects.get(id=booking_id)
            
            # Confirm the booking
            booking.confirm_booking()  # Update status to confirmed
            
            # Send confirmation email
            self._send_confirmation_email(booking)
            
            logger.info(f"Booking {booking_id} confirmed and email sent.")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Booking confirmed',
                status=200)
        except Booking.DoesNotExist:
            logger.error(f"Booking with ID {booking_id} not found.")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: Booking not found',
                status=500)
        except Exception as e:
            # Log any other unexpected errors
            logger.error(f"An error occurred while processing booking {booking_id}: {e}")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: {str(e)}',
                status=500)

    def handle_payment_intent_payment_failed(self, event):
        """Handles the payment_intent.payment_failed webhook from Stripe."""
        logger.warning(f"Payment failed: {event['type']}")
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    
    def handle_checkout_session_completed(self, event):
        """Handles the checkout.session.completed webhook from Stripe."""
        session = event.data.object
        logger.info(f"Checkout session completed: {json.dumps(session, indent=2)}")

        # Retrieve the booking ID from metadata
        booking_id = session.client_reference_id

        try:
            # Fetch the booking associated with this payment
            booking = Booking.objects.get(id=booking_id)
            booking.confirm_booking()  # Update status to confirmed
            self._send_confirmation_email(booking)
            logger.info(f"Booking {booking_id} confirmed and email sent.")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Booking confirmed',
                status=200)
        except Booking.DoesNotExist:
            logger.error(f"Booking with ID {booking_id} not found.")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: Booking not found',
                status=500)
        
    def handle_checkout_session_async_payment_failed(self, event):
        """Handles the checkout.session.async_payment_failed webhook from Stripe."""
        session = event.data.object
        logger.warning(f"Checkout session payment failed: {json.dumps(session, indent=2)}")

        # Retrieve the booking ID from metadata
        booking_id = session.client_reference_id

        try:
            # Fetch the booking associated with this payment
            booking = Booking.objects.get(id=booking_id)
            booking.cancel_booking()  # Update status to cancelled
            logger.info(f"Booking {booking_id} cancelled due to payment failure.")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Booking cancelled',
                status=200)
        except Booking.DoesNotExist:
            logger.error(f"Booking with ID {booking_id} not found.")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: Booking not found',
                status=500)