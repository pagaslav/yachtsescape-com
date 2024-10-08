# yachts/views.py

from django.shortcuts import render, get_object_or_404
from .models import Yacht

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

    return render(request, 'yachts/yacht-list.html', {'yachts': yachts})