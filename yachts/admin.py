from django.contrib import admin
from django import forms
from .models import Yacht

class YachtAdminForm(forms.ModelForm):
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
    form = YachtAdminForm
    list_display = ('name', 'id', 'type', 'description', 'country', 'location', 'capacity', 'price_per_day', 'rating', 'image_path')

    def image_path(self, obj):
        return obj.card_image.url if obj.card_image else "No image"
    image_path.short_description = 'Image Path'

    def detail_image_path(self, obj):
        return obj.detail_image.url if obj.detail_image else "No detail image"
    detail_image_path.short_description = 'Detail Image Path'

admin.site.register(Yacht, YachtAdmin)