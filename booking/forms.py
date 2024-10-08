# booking/forms.py

from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['yacht_type', 'capacity', 'start_date', 'end_date']

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if start_date < date.today():
            raise ValidationError("Start date cannot be in the past.")
        return start_date

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise ValidationError("End date must be after the start date.")
        
        return cleaned_data