""" booking/apps.py """

from django.apps import AppConfig


class BookingConfig(AppConfig):
    """ Configuration class for the Booking app """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
