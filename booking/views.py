# booking/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages  # Import messages for displaying notifications
from .forms import BookingForm  # Import the booking form
from yachts.models import Yacht  # Import the yacht model
from datetime import datetime


def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Associate booking with the current user
            
            # Get yacht ID and date range
            yacht_id = request.POST.get('yacht')
            date_range = request.POST.get('date_range', '').split(' to ')
            
            if yacht_id and len(date_range) == 2:
                try:
                    # Associate yacht with booking
                    yacht = get_object_or_404(Yacht, id=yacht_id)
                    booking.yacht = yacht

                    # Parse dates
                    start_date = datetime.strptime(date_range[0], '%Y-%m-%d').date()
                    end_date = datetime.strptime(date_range[1], '%Y-%m-%d').date()

                    # Assign booking dates
                    booking.start_date = start_date
                    booking.end_date = end_date
                    
                    booking.save()
                    print("Booking saved successfully!")  # Confirmation of saving the booking
                    messages.success(request, 'Booking successfully created!')
                    return JsonResponse({'success': True, 'message': 'Booking created successfully.'})

                except Exception as e:
                    print(f"Error saving booking: {e}")
                    messages.error(request, 'An error occurred while saving the booking.')
                    return JsonResponse({'success': False, 'message': 'Error saving booking.'})

            else:
                print("Yacht ID or date range not found.")
                messages.error(request, 'Error creating booking. Yacht or date range not found.')
                return JsonResponse({'success': False, 'message': 'Yacht ID or date range not found.'})

        else:
            print("Form errors:", form.errors)  # Debugging form errors
            messages.error(request, 'Error creating booking. Please check the form.')
            return JsonResponse({'success': False, 'errors': form.errors})

    # If the request is not POST, return an error response
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
