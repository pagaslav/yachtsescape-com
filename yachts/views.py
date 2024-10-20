""" yachts/views.py """

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from .models import Yacht
from booking.models import Booking
from booking.forms import BookingForm
from datetime import datetime
from django.conf import settings

def yacht_list(request):
    """ Returns a list of yachts based on search and filter criteria """
    yachts = Yacht.objects.all()

    filters = []

    boat_type = request.GET.get('type')
    if boat_type:
        yachts = yachts.filter(type__iexact=boat_type)
        filters.append(f"Boat type: {boat_type}")

    country = request.GET.get('country')
    if country:
        yachts = yachts.filter(country=country)
        filters.append(f"Country: {country}")

    location = request.GET.get('location')
    if location:
        yachts = yachts.filter(location__icontains=location)
        filters.append(f"Location: {location}")

    sort_options = {
        'price_low': 'price_per_day',
        'price_high': '-price_per_day',
        'rating_low': 'rating',
        'rating_high': '-rating',
    }
    
    sort_names = {
        'price_low': 'Price: Low to High',
        'price_high': 'Price: High to Low',
        'rating_low': 'Rating: Low to High',
        'rating_high': 'Rating: High to Low',
        'type_az': 'Type: A to Z',
    }

    sort = request.GET.get('sort')
    if sort in sort_options:
        yachts = yachts.order_by(sort_options[sort])
        filters.append(f"Sorted by: {sort_names.get(sort, 'Unknown sort option')}")

    capacity_filter = {
        '2-8': {'capacity__lte': 8},
        '8_plus': {'capacity__gt': 8},
    }
    capacity = request.GET.get('capacity')
    if capacity in capacity_filter:
        yachts = yachts.filter(**capacity_filter[capacity])
        filters.append(f"Capacity: {capacity}")

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
        yachts = yachts.exclude(
            bookings__start_date__lt=end_date,
            bookings__end_date__gt=start_date
        )
        filters.append(f"Available between: {start_date} and {end_date}")

    if not yachts:
        message = (
            "Unfortunately, there are no yachts available for your "
            "search criteria."
        )
    else:
        message = None

    filters_title = ", ".join(filters) if filters else "All yachts"

    return render(request, 'yachts/yacht-list.html', {
        'yachts': yachts,
        'message': message,
        'filters_title': filters_title
    })

def yacht_booking_dates(request, yacht_id):
    """ Returns the booked dates for a specific yacht """
    yacht = get_object_or_404(Yacht, id=yacht_id)
    bookings = Booking.objects.filter(
        yacht=yacht, status='confirmed'
    ).values('start_date', 'end_date')
    booked_dates = []
    for booking in bookings:
        start_date = booking['start_date']
        end_date = booking['end_date']
        if isinstance(start_date, datetime):
            start_date_str = start_date.strftime('%Y-%m-%d')
        else:
            start_date_str = start_date
        if isinstance(end_date, datetime):
            end_date_str = end_date.strftime('%Y-%m-%d')
        else:
            end_date_str = end_date
        booked_dates.append({'start': start_date_str, 'end': end_date_str})

    return JsonResponse({'booked_dates': booked_dates})

def yacht_detail(request, yacht_id):
    """ Renders the details of a specific yacht along with its booking form """
    yacht = get_object_or_404(Yacht, id=yacht_id)
    bookings = Booking.objects.filter(
        yacht=yacht, status='confirmed'
    ).values('start_date', 'end_date')
    booked_dates = []
    for booking in bookings:
        start_date = booking['start_date']
        end_date = booking['end_date']
        if isinstance(start_date, datetime):
            start_date_str = start_date.strftime('%Y-%m-%d')
        else:
            start_date_str = start_date
        if isinstance(end_date, datetime):
            end_date_str = end_date.strftime('%Y-%m-%d')
        else:
            end_date_str = end_date
        booked_dates.append({'start': start_date_str, 'end': end_date_str})

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.yacht = yacht
            booking.user = request.user
            date_range = form.cleaned_data['date_range']
            start_date_str, end_date_str = date_range.split(" to ")
            booking.start_date = datetime.strptime(
                start_date_str, '%Y-%m-%d'
            ).date()
            booking.end_date = datetime.strptime(
                end_date_str, '%Y-%m-%d'
            ).date()
            booking.save()
    else:
        form = BookingForm()

    context = {
        'yacht': yacht,
        'booked_dates': booked_dates,
        'form': form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }

    return render(request, 'yachts/yacht_detail.html', context)

class YachtImageView(View):
    """ Provides a JSON response with the images for a specific yacht """
    def get(self, request, yacht_id):
        yacht = get_object_or_404(Yacht, id=yacht_id)
        images = yacht.get_detail_images()
        return JsonResponse(images, safe=False)