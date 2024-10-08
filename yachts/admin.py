# yachts/admin.py

from django.contrib import admin
from .models import Yacht

class YachtAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'type', 'description', 'country', 'location', 'capacity', 'price_per_day', 'rating', 'available', 'image')

admin.site.register(Yacht, YachtAdmin)