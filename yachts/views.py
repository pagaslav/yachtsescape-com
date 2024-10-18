# yachts/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from .models import Yacht
from booking.models import Booking
from booking.forms import BookingForm  # Import the booking form
from datetime import datetime
from django.conf import settings

# View to display a list of yachts
def yacht_list(request):
    yachts = Yacht.objects.all() 
    # Filter by boat type from the search form
    boat_type = request.GET.get('type') 
    if boat_type:
        yachts = yachts.filter(type__iexact=boat_type) 

    # Filter by country
    country = request.GET.get('country') 
    if country:
        yachts = yachts.filter(country=country) 

    # Filter by location
    location = request.GET.get('location') 
    if location:
        yachts = yachts.filter(location__icontains=location) 

    # Sorting options
    sort_options = {
        'price_low': 'price_per_day', 
        'price_high': '-price_per_day', 
        'rating_low': 'rating',  
        'rating_high': '-rating', 
    }
    sort = request.GET.get('sort')
    if sort in sort_options:
        yachts = yachts.order_by(sort_options[sort])

    # Capacity filtering based on the search form
    capacity_filter = {
        '2-8': {'capacity__lte': 8},
        '8_plus': {'capacity__gt': 8}, 
    }
    capacity = request.GET.get('capacity')
    if capacity in capacity_filter:
        yachts = yachts.filter(**capacity_filter[capacity])

    # Date filtering to exclude yachts booked during the selected dates
    start_date = request.GET.get('start_date') 
    end_date = request.GET.get('end_date') 
    if start_date and end_date:
        yachts = yachts.exclude(
            bookings__start_date__lt=end_date,
            bookings__end_date__gt=start_date
        )

    return render(request, 'yachts/yacht-list.html', {'yachts': yachts})

def yacht_booking_dates(request, yacht_id):
    # Get the yacht object or return a 404 if not found
    yacht = get_object_or_404(Yacht, id=yacht_id)
    
    # Filter bookings for the specific yacht that have a confirmed status
    bookings = Booking.objects.filter(yacht=yacht, status='confirmed').values('start_date', 'end_date')

    # Create a list of booked dates to pass as JSON response
    booked_dates = []
    for booking in bookings:
        start_date = booking['start_date']
        end_date = booking['end_date']
        
        # Convert to string if they are datetime.date objects
        if isinstance(start_date, datetime):
            start_date_str = start_date.strftime('%Y-%m-%d')
        else:
            start_date_str = start_date

        if isinstance(end_date, datetime):
            end_date_str = end_date.strftime('%Y-%m-%d')
        else:
            end_date_str = end_date

        booked_dates.append({
            'start': start_date_str,
            'end': end_date_str
        })

    # Return the booked dates as JSON
    return JsonResponse({'booked_dates': booked_dates})

# View to display yacht details and handle booking form submission
def yacht_detail(request, yacht_id):
    yacht = get_object_or_404(Yacht, id=yacht_id)
    
    # Retrieve bookings for the yacht with confirmed status
    bookings = Booking.objects.filter(yacht=yacht, status='confirmed').values('start_date', 'end_date')

    # Create a list of booked dates to pass to the template
    booked_dates = []
    for booking in bookings:
        start_date = booking['start_date']
        end_date = booking['end_date']
        
        # Check if start_date and end_date are datetime.date objects
        print(f"Start Date Type: {type(start_date)}, End Date Type: {type(end_date)}")
        
        # Convert to string if they are datetime.date objects
        if isinstance(start_date, datetime):
            start_date_str = start_date.strftime('%Y-%m-%d')
        else:
            start_date_str = start_date  

        if isinstance(end_date, datetime):
            end_date_str = end_date.strftime('%Y-%m-%d')
        else:
            end_date_str = end_date  

        booked_dates.append({
            'start': start_date_str,
            'end': end_date_str
        })

    print("Booked Dates List:", booked_dates)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.yacht = yacht
            booking.user = request.user 
            
            # Get date range from the form
            date_range = form.cleaned_data['date_range']
            
            # Split the range into start and end dates
            start_date_str, end_date_str = date_range.split(" to ")
            
            # Convert strings to date objects
            booking.start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            booking.end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            
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

# View to return yacht images as JSON
class YachtImageView(View):
    def get(self, request, yacht_id):
        yacht = get_object_or_404(Yacht, id=yacht_id) 
        images = yacht.get_detail_images()  
        return JsonResponse(images, safe=False) 