# yachts/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Yacht
from booking.models import Booking
from booking.forms import BookingForm  # Импортируем форму бронирования
from datetime import datetime

# View to display a list of yachts
def yacht_list(request):
    yachts = Yacht.objects.all()  # Initial query to get all yachts

    # Filter by boat type from the search form
    boat_type = request.GET.get('type')  # Get the selected boat type from the GET request
    if boat_type:
        yachts = yachts.filter(type__iexact=boat_type)  # Filter yachts by the selected boat type

    # Filter by country
    country = request.GET.get('country')  # Get the selected country from the GET request
    if country:
        yachts = yachts.filter(country=country)  # Filter yachts by the selected country

    # Filter by location
    location = request.GET.get('location')  # Get the selected location from the GET request
    if location:
        yachts = yachts.filter(location__icontains=location)  # Filter yachts by the selected location

    # Sorting options
    sort_options = {
        'price_low': 'price_per_day',  # Sort by price ascending
        'price_high': '-price_per_day',  # Sort by price descending
        'rating_low': 'rating',  # Sort by rating ascending
        'rating_high': '-rating',  # Sort by rating descending
        'name_az': 'name',  # Sort by name A-Z
        'name_za': '-name',  # Sort by name Z-A
        'type_az': 'type',  # Sort by type A-Z
        'type_za': '-type'  # Sort by type Z-A
    }
    sort = request.GET.get('sort')  # Get the selected sorting option from the GET request
    if sort in sort_options:
        yachts = yachts.order_by(sort_options[sort])  # Apply sorting based on the selected option

    # Capacity filtering based on the search form
    capacity_filter = {
        '2-4': {'capacity__lte': 4},  # Filter for capacity up to 4
        '4-6': {'capacity__gte': 4, 'capacity__lte': 6},  # Filter for capacity between 4 and 6
        '6-8': {'capacity__gte': 6, 'capacity__lte': 8},  # Filter for capacity between 6 and 8
        '8_plus': {'capacity__gt': 8},  # Filter for capacity greater than 8
    }
    capacity = request.GET.get('capacity')  # Get the selected capacity from the GET request
    if capacity in capacity_filter:
        yachts = yachts.filter(**capacity_filter[capacity])  # Apply filtering based on the selected capacity

    # Date filtering to exclude yachts booked during the selected dates
    start_date = request.GET.get('start_date')  # Get the selected start date from the GET request
    end_date = request.GET.get('end_date')  # Get the selected end date from the GET request
    if start_date and end_date:
        yachts = yachts.exclude(
            bookings__start_date__lt=end_date,
            bookings__end_date__gt=start_date
        )  # Exclude yachts that are booked during the selected dates

    return render(request, 'yachts/yacht-list.html', {'yachts': yachts})

def yacht_detail(request, yacht_id):
    yacht = get_object_or_404(Yacht, id=yacht_id)
    bookings = Booking.objects.filter(yacht=yacht).values('start_date', 'end_date')

   # Формируем список занятых дат для передачи в шаблон
    booked_dates = []
    for booking in bookings:
        start_date = booking['start_date']
        end_date = booking['end_date']
        
        # Проверяем, являются ли start_date и end_date объектами datetime.date
        print(f"Start Date Type: {type(start_date)}, End Date Type: {type(end_date)}")
        
        # Если это объекты datetime.date, преобразуем их в строки
        if isinstance(start_date, datetime):
            start_date_str = start_date.strftime('%Y-%m-%d')
        else:
            start_date_str = start_date  # Если это уже строка

        if isinstance(end_date, datetime):
            end_date_str = end_date.strftime('%Y-%m-%d')
        else:
            end_date_str = end_date  # Если это уже строка

        booked_dates.append({
            'start': start_date_str,
            'end': end_date_str
        })
    print("Booked Dates List:", booked_dates)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.yacht = yacht  # Устанавливаем текущую яхту
            booking.user = request.user  # Устанавливаем текущего пользователя
            
            # Получаем диапазон дат из формы
            date_range = form.cleaned_data['date_range']
            
            # Разделяем диапазон на начальную и конечную даты
            start_date_str, end_date_str = date_range.split(" to ")
            
            # Преобразуем строки в объекты даты
            booking.start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            booking.end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            
            booking.save()  # Сохраняем объект бронирования
            return redirect('booking_success')  # Перенаправляем на страницу успешного бронирования

    else:
        form = BookingForm()

    context = {
        'yacht': yacht,
        'booked_dates': booked_dates,
        'form': form,  # Передаём форму в контекст
    }

    return render(request, 'yachts/yacht_detail.html', context)