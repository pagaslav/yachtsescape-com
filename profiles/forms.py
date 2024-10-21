# profiles/forms.py

from django import forms
from .models import UserProfile
from yachts.models import Yacht

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'street_address1',
            'street_address2',
            'town_city',
            'county_state',
            'postal_code',
            'country',
        ]

from django import forms
from yachts.models import Yacht

class YachtForm(forms.ModelForm):
    class Meta:
        model = Yacht
        fields = [
            'name',
            'type',
            'description',
            'country',
            'location',
            'capacity',
            'price_per_day',
            'rating',
            'card_image',
            'detail_image1',
            'detail_image2',
            'detail_image3',
        ]