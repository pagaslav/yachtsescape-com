# yachts/admin.py

from django.contrib import admin
from .models import Yacht

class YachtAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'type', 'description', 'country', 'location', 'capacity', 'price_per_day', 'rating', 'image_path')

    def image_path(self, obj):
        return obj.card_image.url if obj.card_image else "No image"
    image_path.short_description = 'Image Path'

    def detail_image_path(self, obj):
        return obj.detail_image.url if obj.detail_image else "No detail image"
    detail_image_path.short_description = 'Detail Image Path'

admin.site.register(Yacht, YachtAdmin)