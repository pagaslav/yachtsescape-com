""" checkout/webhooks.py """

import logging
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from booking.webhook_handler import StripeWH_Handler
import stripe

# Set the Stripe API version
stripe.api_version = settings.STRIPE_API_VERSION

logger = logging.getLogger(__name__)


@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe."""
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        # Verify the event by checking its signature
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
        logger.info(f"Received Stripe event: {event['type']}")
    except ValueError:
        # Handle invalid payload
        logger.error("Invalid payload")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Handle invalid signature
        logger.error("Invalid signature")
        return HttpResponse(status=400)
    except Exception as e:
        # Handle any unknown errors
        logger.error(f"Unknown error occurred: {e}")
        return HttpResponse(status=400)

    # Set up a webhook handler
    handler = StripeWH_Handler(request)

    event_map = {
        'payment_intent.succeeded':
            handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed':
            handler.handle_payment_intent_payment_failed,
        'checkout.session.completed':
            handler.handle_checkout_session_completed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)
    return response
