""" booking/views.py """

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Booking
from profiles.models import UserProfile
from .forms import BookingForm
from yachts.models import Yacht
from datetime import datetime
from django.conf import settings
import stripe

# Set the Stripe secret key and version
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def booking_create(request):
    """ Create a new booking and initiate Stripe session """

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user

            yacht_id = request.POST.get('yacht')
            date_range = request.POST.get('date_range', '').split(' to ')

            if yacht_id and len(date_range) >= 1:
                try:
                    # Get the yacht by ID
                    yacht = get_object_or_404(Yacht, id=yacht_id)
                    booking.yacht = yacht

                    # Parse start and end dates
                    start_date = datetime.strptime(
                        date_range[0], '%Y-%m-%d'
                    ).date()
                    end_date = (
                        start_date if len(date_range) == 1 else
                        datetime.strptime(date_range[1], '%Y-%m-%d').date()
                    )

                    booking.start_date = start_date
                    booking.end_date = end_date
                    booking.save()

                    # Prepare line items for Stripe
                    line_items = [{
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': f"Yacht Rental - {yacht.name}",
                                'description': (
                                    f"Rental from {start_date} "
                                    f"to {end_date}"
                                ),
                            },
                            'unit_amount': int(booking.total_cost * 100),
                        },
                        'quantity': 1,
                    }]

                    # Create Stripe session
                    checkout_session = stripe.checkout.Session.create(
                        payment_method_types=['card'],
                        line_items=line_items,
                        mode='payment',
                        success_url=(
                            f"https://{settings.MYSITE_DOMAIN}/booking/"
                            f"booking_success/{booking.id}/"
                        ),
                        cancel_url=(
                            f"https://{settings.MYSITE_DOMAIN}/yachts/"
                            f"yacht/{yacht.id}/"
                        ),
                        client_reference_id=booking.id,
                        payment_intent_data={
                            'metadata': {
                                'booking_id': booking.id
                            }
                        }
                    )

                    # Return Stripe Checkout URL
                    return JsonResponse({
                        'success': True,
                        'redirect_url': checkout_session.url
                    })

                except stripe.error.StripeError as e:
                    # Handle Stripe errors
                    print(f"Stripe error: {e}")
                    return JsonResponse({
                        'error': (
                            'Payment processing error. Try again later.'
                        )
                    }, status=500)
                except Exception as e:
                    # Handle other errors
                    print(f"Error details: {e}")
                    return JsonResponse({
                        'error': (
                            'Error creating the booking.'
                        )
                    }, status=500)
            else:
                # Missing yacht ID or date range
                return JsonResponse({
                    'error': 'Yacht ID or date range missing.'
                }, status=400)
        else:
            # Form validation failed
            return JsonResponse({
                'error': 'Invalid form data.',
                'form_errors': form.errors
            }, status=400)

    # Only allow POST requests
    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def booking_success(request, booking_id):
    """ Display booking success page """

    booking = get_object_or_404(Booking, id=booking_id)
    profiles = get_object_or_404(UserProfile, user=booking.user)

    return render(request, 'booking/booking_success.html', {
        'booking': booking,
        'profiles': profiles,
    })
