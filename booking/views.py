# booking/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .forms import BookingForm
from yachts.models import Yacht
from datetime import datetime
from django.urls import reverse

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            
            # Get yacht ID and date range
            yacht_id = request.POST.get('yacht')
            date_range = request.POST.get('date_range', '').split(' to ')
            
            if yacht_id and len(date_range) >= 1:  # Make sure at least one date is provided
                try:
                    yacht = get_object_or_404(Yacht, id=yacht_id)
                    booking.yacht = yacht

                    # Parse start date
                    start_date = datetime.strptime(date_range[0], '%Y-%m-%d').date()

                    # If only one date is provided, treat it as both start and end date
                    if len(date_range) == 1:
                        end_date = start_date
                    else:
                        end_date = datetime.strptime(date_range[1], '%Y-%m-%d').date()

                    booking.start_date = start_date
                    booking.end_date = end_date
                    
                    # Save the booking instance
                    booking.save()
                    messages.success(request, 'Booking successfully created!')

                    # Return a JSON response with the URL to redirect
                    return JsonResponse({
                        'success': True,
                        'redirect_url': reverse('checkout', args=[booking.id, start_date, end_date])
                    })

                except Exception as e:
                    print(f"Error saving booking: {e}")
                    messages.error(request, 'An error occurred while saving the booking.')
                    return JsonResponse({'success': False, 'message': 'Error saving booking.'})

            else:
                print("Yacht ID or date range not found.")
                messages.error(request, 'Error creating booking. Yacht or date range not found.')
                return JsonResponse({'success': False, 'message': 'Yacht ID or date range not found.'})

        else:
            print("Form errors:", form.errors)
            messages.error(request, 'Error creating booking. Please check the form.')
            return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
