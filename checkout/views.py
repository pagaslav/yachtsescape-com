# checkout/views.py

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order
from booking.models import Booking
from profiles.models import UserProfile
import stripe
import json

# View to handle caching of checkout data for Stripe
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Adding metadata to Stripe's PaymentIntent for tracking
        stripe.PaymentIntent.modify(pid, metadata={
            'booking_id': request.POST.get('booking_id'),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        # Handling payment error and sending a response
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

# Main checkout view responsible for displaying the form and processing the order
def checkout(request, booking_id, start_date, end_date):  # Add start_date and end_date here
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Retrieve the selected booking by its ID
    booking = get_object_or_404(Booking, id=booking_id)
    yacht = booking.yacht

    if request.method == 'POST':
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
            # If the form is valid, save the order without committing to database
            order = order_form.save(commit=False)
            order.booking = booking  # Link the booking to the order
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid  # Store the Stripe PaymentIntent ID for reference
            order.total_cost = booking.total_cost  # Set the total cost from the booking
            order.save()  # Save the order to the database
            
            # Redirect to a success page after checkout is completed
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            # If the form is not valid, return an error message
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        # If the request is GET, prepare the checkout form with initial data
        order_form = OrderForm()

        # Set up Stripe payment intent
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=int(booking.total_cost * 100),  # Convert cost to cents for Stripe
            currency=settings.STRIPE_CURRENCY,
        )

        print(intent)

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,  # Include Stripe client secret for frontend
        'booking': booking,
        'yacht': yacht,
        'start_date': start_date,  # Pass start_date to context if needed
        'end_date': end_date,      # Pass end_date to context if needed
    }

    return render(request, template, context)