# checkout/webhook_handler.py

import json
import logging
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from booking.models import Booking
from django.utils.timezone import now

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
        intent = event.data.object
        logger.info(f"Intent data: {json.dumps(intent, indent=2)}")

        # Retrieve the booking ID from metadata
        booking_id = intent.metadata.get('booking_id')

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

    def handle_payment_intent_payment_failed(self, event):
        """Handles the payment_intent.payment_failed webhook from Stripe."""
        logger.warning(f"Payment failed: {event['type']}")
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)