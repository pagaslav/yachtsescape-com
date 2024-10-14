# checkout/views.py

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order
from booking.models import Booking
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import stripe
stripe.api_version = "2024-06-20"

# View to handle caching of checkout data for Stripe
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        print("Received client_secret for caching:", pid)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Adding metadata to Stripe's PaymentIntent for tracking
        stripe.PaymentIntent.modify(pid, metadata={
            'booking_id': request.POST.get('booking_id'),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        print("Successfully cached checkout data")
        return HttpResponse(status=200)
    except Exception as e:
        print("Error in cache_checkout_data:", e)
        # Handling payment error and sending a response
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

# Main checkout view responsible for displaying the form and processing the order
def checkout(request, booking_id, start_date, end_date):  # Add start_date and end_date here
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Initialize intent as None
    intent = None

    # Retrieve the selected booking by its ID
    booking = get_object_or_404(Booking, id=booking_id)
    yacht = booking.yacht

    # Check if an order already exists for this booking
    existing_order = Order.objects.filter(booking=booking).first()
    if existing_order:
        # Redirect to the existing order or display a message
        messages.info(request, "An order for this booking already exists.")
        return redirect(reverse('checkout_success', args=[existing_order.order_number]))

    if request.method == 'POST':
        print("Received POST data:", request.POST)
        # Store form data in a dictionary to validate later
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        
        # Initialize the order form with the submitted data
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            print("Order form is valid")
            # If the form is valid, save the order without committing to database
            order = order_form.save(commit=False)
            order.booking = booking  # Link the booking to the order
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid  # Store the Stripe PaymentIntent ID for reference
            order.total_cost = booking.total_cost  # Set the total cost from the booking
            try:
                order.save()  # Save the order to the database
                print("Order saved successfully:", order)
            except IntegrityError:
                print("IntegrityError: Order for this booking already exists")
                messages.error(request, "An order for this booking already exists.")
                return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            # If the form is not valid, return an error message
            print("Order form is not valid:", order_form.errors)
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        # If the request is GET, prepare the checkout form with initial data
        order_form = OrderForm()

        # Set up Stripe payment intent
        stripe.api_key = stripe_secret_key
        print("Creating PaymentIntent with amount:", int(booking.total_cost * 100), "and currency:", settings.STRIPE_CURRENCY)
        intent = stripe.PaymentIntent.create(
            amount=int(booking.total_cost * 100),  # Convert cost to cents for Stripe
            currency=settings.STRIPE_CURRENCY,
        )

        print("PaymentIntent created successfully:", intent if intent else "Failed to create PaymentIntent")

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'

    client_secret_value = intent.client_secret if intent else ''


    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret_value,  # Include Stripe client secret for frontend
        'booking': booking,
        'yacht': yacht,
        'start_date': start_date,  # Pass start_date to context if needed
        'end_date': end_date,      # Pass end_date to context if needed
    }

    return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    profile = UserProfile.objects.get(user=request.user)
    # Attach the user's profile to the order
    order.user_profile = profile
    order.save()

    # Save the user's info
    if save_info:
        profile_data = {
            'default_phone_number': order.phone_number,
            'default_country': order.country,
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_county': order.county,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')


    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


@csrf_exempt
def webhook(request):
    # Retrieve the event by verifying the webhook signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WH_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Set up a Stripe webhook handler
    wh_handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': wh_handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': wh_handler.handle_payment_intent_payment_failed,
    }

    # Get the event type from Stripe
    event_type = event['type']

    # If there's a handler for the event, get it from the event map, else use the generic one
    event_handler = event_map.get(event_type, wh_handler.handle_event)

    # Call the event handler
    response = event_handler(event)
    return response