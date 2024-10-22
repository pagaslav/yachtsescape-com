"""
yachts/admin.py
"""

from django.contrib import admin
from django import forms
from .models import Yacht

class YachtAdminForm(forms.ModelForm):
    """ Custom form for Yacht admin panel with specific labels """
    class Meta:
        model = Yacht
        fields = '__all__'
        labels = {
            'card_image': 'Add Yacht Card Image',
            'detail_image1': 'Add First Detail Image',
            'detail_image2': 'Add Second Detail Image',
            'detail_image3': 'Add Third Detail Image',
        }

class YachtAdmin(admin.ModelAdmin):
    """ Custom admin panel for Yacht model """
    form = YachtAdminForm
    list_display = (
        'name', 'id', 'type', 'description', 'country', 'location',
        'capacity', 'price_per_day', 'rating', 'image_path'
    )

    def image_path(self, obj):
        """ Returns the card image URL or 'No image' if absent """
        return obj.card_image.url if obj.card_image else "No image"
    image_path.short_description = 'Image Path'

    def detail_image_path(self, obj):
        """ Returns the detail image URL or 'No detail image' if absent """
        return obj.detail_image.url if obj.detail_image else "No detail image"
    detail_image_path.short_description = 'Detail Image Path'

admin.site.register(Yacht, YachtAdmin)
