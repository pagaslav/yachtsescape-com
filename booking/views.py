from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import reverse
from .models import Booking
from profiles.models import UserProfile
from .forms import BookingForm
from yachts.models import Yacht
from datetime import datetime
from django.conf import settings
import stripe

# Set the Stripe secret key for API access
stripe.api_key = settings.STRIPE_SECRET_KEY

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            # Prepare the booking object without saving to the database yet
            booking = form.save(commit=False)
            booking.user = request.user  # Associate the booking with the logged-in user

            yacht_id = request.POST.get('yacht')
            date_range = request.POST.get('date_range', '').split(' to ')
            
            # Ensure yacht ID and a date range are provided
            if yacht_id and len(date_range) >= 1:
                try:
                    yacht = get_object_or_404(Yacht, id=yacht_id)
                    booking.yacht = yacht

                    # Parse start and end dates from the date range
                    start_date = datetime.strptime(date_range[0], '%Y-%m-%d').date()
                    end_date = start_date if len(date_range) == 1 else datetime.strptime(date_range[1], '%Y-%m-%d').date()
                    
                    booking.start_date = start_date
                    booking.end_date = end_date
                    booking.save()

                    # Prepare line items for Stripe
                    line_items = [{
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': f"Yacht Rental - {yacht.name}",
                                'description': f"Rental from {start_date} to {end_date}",
                            },
                            'unit_amount': int(booking.total_cost * 100),  # Ensure total_cost is in cents
                        },
                        'quantity': 1,
                    }]

                    # Create the Stripe checkout session
                    checkout_session = stripe.checkout.Session.create(
                        payment_method_types=['card'],
                        line_items=line_items,
                        mode='payment',
                        success_url=f"https://{settings.MYSITE_DOMAIN}/booking/booking_success/{booking.id}/",
                        cancel_url=f"https://{settings.MYSITE_DOMAIN}/yachts/yacht/{yacht.id}/",
                        client_reference_id=booking.id,
                          metadata={
                                'booking_id': booking.id  # Add booking_id to the session metadata
                            }  # Pass the booking ID here
                    )

                    # Redirect the user to the Stripe Checkout URL
                    return JsonResponse({'success': True, 'redirect_url': checkout_session.url})
                
                except stripe.error.StripeError as e:
                    # Handle Stripe-specific errors
                    print(f"Stripe error: {e}")
                    return JsonResponse({'error': 'Payment processing error. Please try again later.'}, status=500)
                except Exception as e:
                    # Log any other errors and return an error message
                    print(f"Error details: {e}")
                    return JsonResponse({'error': 'An error occurred while creating the booking.'}, status=500)
            else:
                return JsonResponse({'error': 'Yacht ID or date range not provided.'}, status=400)
        else:
            # Return form errors if the form is not valid
            return JsonResponse({'error': 'Invalid form data.', 'form_errors': form.errors}, status=400)
    
    # Return an error if the request method is not POST
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

# View to show booking success page
def booking_success(request, booking_id):
    # Retrieve the booking object based on the booking ID
    booking = get_object_or_404(Booking, id=booking_id)
    # Fetch the user profile based on the booking's user
    profiles = get_object_or_404(UserProfile, user=booking.user)

    # Render a success page to the user with booking details
    return render(request, 'booking/booking_success.html', {
        'booking': booking,
        'profiles': profiles,
    })