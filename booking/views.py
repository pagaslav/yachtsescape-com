# booking/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # For displaying success messages
from .forms import BookingForm  # Import the booking form
from yachts.models import Yacht  # Import the yacht model

def booking_create(request):
    # Process POST request for booking
    if request.method == 'POST':
        form = BookingForm(request.POST)  # Create a form with POST data
        if form.is_valid():  # Validate the form
            booking = form.save(commit=False)  # Create booking object but don't save to DB yet
            booking.user = request.user  # Assign the current user to the booking
            booking.save()  # Save the booking object to the DB
            messages.success(request, 'Your booking was successful!')  # Display success message
            return redirect('home')  # Redirect to home or another page
    else:
        form = BookingForm()  # Create an empty form if not a POST request

    return render(request, 'booking/booking-form.html', {'form': form})  # Render the booking form template

def filter_yachts(request):
    # Логика фильтрации будет здесь
    return render(request, 'booking/yacht_list.html')

def yacht_detail(request, yacht_id):
    yacht = get_object_or_404(Yacht, id=yacht_id)  # Retrieve the yacht or show 404 if not found

    # Handle booking form submission
    if request.method == 'POST':
        form = BookingForm(request.POST)  # Create a form with POST data
        if form.is_valid():  # Validate the form
            booking = form.save(commit=False)  # Create booking object but don't save to DB yet
            booking.yacht = yacht  # Assign the yacht to the booking
            booking.user = request.user  # Assign the current user to the booking
            booking.save()  # Save the booking object to the DB
            messages.success(request, 'Your booking was successful!')  # Display success message
            return redirect('yacht_detail', yacht_id=yacht.id)  # Redirect back to yacht detail page
    else:
        form = BookingForm()  # Create an empty form if not a POST request

    # Render yacht detail template with the yacht and booking form
    return render(request, 'yachts/yacht_detail.html', {'yacht': yacht, 'form': form})