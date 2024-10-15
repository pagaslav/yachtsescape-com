# profiles/forms.py

from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'street_address1', 'street_address2', 
                  'town_city', 'county_state', 'postal_code', 'country']