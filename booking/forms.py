
# booking/forms.py

from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from datetime import date, datetime

class BookingForm(forms.ModelForm):
    date_range = forms.CharField(label='Select Dates', required=True)

    class Meta:
        model = Booking
        fields = ['yacht', 'date_range']

    def clean_date_range(self):
        date_range = self.cleaned_data.get('date_range')
        if date_range:
            try:
                start_date_str, end_date_str = date_range.split(" to ")
                start_date = datetime.strptime(start_date_str.strip(), '%Y-%m-%d').date()
                end_date = datetime.strptime(end_date_str.strip(), '%Y-%m-%d').date()
                
                if start_date < date.today():
                    raise ValidationError("Start date cannot be in the past.")
                
                if start_date > end_date:
                    raise ValidationError("End date must be after the start date.")
                
                self.cleaned_data['start_date'] = start_date
                self.cleaned_data['end_date'] = end_date
            except ValueError:
                raise ValidationError("Invalid date format. Use the format 'YYYY-MM-DD to YYYY-MM-DD'.")
        return date_range

    def clean(self):
        cleaned_data = super().clean()
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise ValidationError("End date must be after the start date.")
        
        return cleaned_data