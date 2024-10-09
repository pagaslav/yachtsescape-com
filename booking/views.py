# booking/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # Import messages for displaying notifications
from .forms import BookingForm  # Import the booking form
from yachts.models import Yacht  # Import the yacht model
from datetime import datetime



def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Привязываем бронирование к текущему пользователю
            
            # Получаем идентификатор яхты
            yacht_id = request.POST.get('yacht_id')
            date_range = request.POST.get('date_range', '').split(' to ')
            
            if yacht_id and len(date_range) == 2:
                try:
                    # Привязываем яхту к бронированию
                    yacht = get_object_or_404(Yacht, id=yacht_id)
                    booking.yacht = yacht

                    # Парсим даты
                    start_date = datetime.strptime(date_range[0], '%Y-%m-%d').date()
                    end_date = datetime.strptime(date_range[1], '%Y-%m-%d').date()

                    # Присваиваем даты бронирования
                    booking.start_date = start_date
                    booking.end_date = end_date
                    
                    booking.save()
                    print("Booking saved successfully!")  # Подтверждение сохранения бронирования
                    messages.success(request, 'Booking successfully created!')
                    return redirect('yacht_detail', yacht_id=yacht.id)
                
                except Exception as e:
                    print(f"Error saving booking: {e}")
                    messages.error(request, 'An error occurred while saving the booking.')
            else:
                print("Yacht ID or date range not found.")
                messages.error(request, 'Error creating booking. Yacht or date range not found.')
                return redirect('yacht_list')

        else:
            print("Form errors:", form.errors)  # Отладка ошибок формы
            messages.error(request, 'Error creating booking. Please check the form.')

    # Переход на страницу деталей яхты, если бронирование не удалось
    yacht_id = request.POST.get('yacht_id')
    if yacht_id:
        return redirect('yacht_detail', yacht_id=yacht_id)
    else:
        return redirect('yacht_list')

def filter_yachts(request):
    """
    Display a list of yachts with applied filters.
    """
    # The filtering logic will be here
    return render(request, 'booking/yacht_list.html')

def yacht_detail(request, yacht_id):
    """
    Display details of a specific yacht, including the booking form.
    """
    yacht = get_object_or_404(Yacht, id=yacht_id)  # Retrieve the yacht or return 404 if not found

    # Handle booking form submission
    if request.method == 'POST':
        form = BookingForm(request.POST)  # Create a form with POST data
        if form.is_valid():  # Validate the form data
            booking = form.save(commit=False)  # Create a booking object without saving it yet
            booking.yacht = yacht  # Associate the booking with the current yacht
            booking.user = request.user  # Associate the booking with the current user
            booking.save()  # Save the booking to the database
            # Display a success message and redirect to yacht detail page
            messages.success(request, 'Your booking was successful!')
            return redirect('yacht_detail', yacht_id=yacht.id)
        else:
            # Display an error message if the form is invalid
            messages.error(request, 'An error occurred. Please check the booking form.')
    else:
        form = BookingForm()  # Provide an empty form for GET requests

    # Render the yacht detail page, passing the yacht and booking form
    return render(request, 'yachts/yacht_detail.html', {'yacht': yacht, 'form': form})