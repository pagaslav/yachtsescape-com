# checkout/forms.py

from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country',
            'county',
        )
        widgets = {
            'total_cost': forms.TextInput(attrs={'readonly': 'readonly'}),  # Make total_cost read-only
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes to fields, remove auto-generated
        labels, and set autofocus on the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
            'total_cost': 'Total Cost',  # Placeholder for total_cost
        }

        # Autofocus on the first field (full_name)
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                # Add '*' to required fields in the placeholder text
                placeholder = placeholders[field]
                if self.fields[field].required:
                    placeholder += ' *'
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Assign a consistent class for styling
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Remove default labels for cleaner form display
            self.fields[field].label = False