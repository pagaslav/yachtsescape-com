# booking/admin.py

from django.contrib import admin
from .models import Booking  # Импортируйте модель Booking

# Зарегистрируйте модель Booking в админке
admin.site.register(Booking)