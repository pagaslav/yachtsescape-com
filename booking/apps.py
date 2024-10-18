# booking/apps.py
from django.apps import AppConfig

class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'

    def ready(self):
        # Import signals to register them
        import booking.signals # noqa: F401