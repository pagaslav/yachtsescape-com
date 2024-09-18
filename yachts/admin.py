from django.contrib import admin
from .models import Yacht

@admin.register(Yacht)
class YachtAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'location', 'capacity', 'price_per_day', 'available'
    )