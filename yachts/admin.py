# yachts/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import Yacht

class YachtAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'type', 'description', 'country', 'location', 'capacity', 'price_per_day', 'rating', 'available', 'thumbnail', 'detail_thumbnail')

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return "-"
    thumbnail.short_description = 'Image'

    def detail_thumbnail(self, obj):
        if obj.detail_image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.detail_image.url)
        return "-"
    detail_thumbnail.short_description = 'Detail Image'

admin.site.register(Yacht, YachtAdmin)