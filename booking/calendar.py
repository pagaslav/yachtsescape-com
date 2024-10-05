# booking/calendar.py

from .models import Booking

def get_yacht_availability(yacht):
    bookings = Booking.objects.filter(yacht=yacht)
    booked_dates = []

    for booking in bookings:
        booked_dates.append({
            'start': booking.start_date,
            'end': booking.end_date,
        })
    
    return booked_dates