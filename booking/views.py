# booking/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # For displaying success messages
from yachts.models import Yacht
from .calendar import get_yacht_availability
from .forms import BookingForm

def yacht_detail(request, yacht_id):
    yacht = get_object_or_404(Yacht, id=yacht_id)
    booked_dates = get_yacht_availability(yacht)

    # Process the booking form submission
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  # Create a booking object but don't save it yet
            booking.yacht = yacht  # Assign the yacht to the booking
            booking.user = request.user  # Assign the current user to the booking
            booking.save()  # Save the booking to the database
            messages.success(request, 'Your booking was successful!')  # Success message
            return redirect('yacht_detail', yacht_id=yacht.id)  # Redirect to yacht detail page
    else:
        form = BookingForm()  # Create an empty form if not a POST request

    # Context for rendering the template
    context = {
        'yacht': yacht,
        'booked_dates': booked_dates,
        'form': form,  # Pass the form to the context
    }
    return render(request, 'yachts/yacht_detail.html', context)