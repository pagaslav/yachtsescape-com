from allauth.account.forms import SignupForm
from django import forms
from profiles.models import UserProfile

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name", required=True)
    last_name = forms.CharField(max_length=30, label="Last Name", required=True)
    phone_number = forms.CharField(
        max_length=15, required=False, label="Phone Number",
        widget=forms.TextInput(attrs={'placeholder': '07990347684'})
    )
    street_address1 = forms.CharField(
        max_length=255, required=True, label="Street Address 1",
        widget=forms.TextInput(attrs={'placeholder': 'Your current address'})
    )
    street_address2 = forms.CharField(
        max_length=255, required=False, label="Street Address 2",
        widget=forms.TextInput(attrs={'placeholder': 'Additional address info'})
    )
    town_city = forms.CharField(
        max_length=50, required=True, label="Town or City",
        widget=forms.TextInput(attrs={'placeholder': 'Town or City'})
    )
    county_state = forms.CharField(
        max_length=50, required=False, label="County, State or Locality",
        widget=forms.TextInput(attrs={'placeholder': 'County or State'})
    )
    postal_code = forms.CharField(
        max_length=20, required=False, label="Postal Code",
        widget=forms.TextInput(attrs={'placeholder': 'e.g., SW1A 1AA'})
    )
    country = forms.CharField(
        max_length=50, required=True, label="Country",
        widget=forms.TextInput(attrs={'placeholder': 'Country'})
    )

    def save(self, request):
        # Save the user first
        user = super(CustomSignupForm, self).save(request)

        # Print statements for debugging purposes
        print("User created:", user)

        # Directly create or update the UserProfile instance associated with the user
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.first_name = self.cleaned_data.get('first_name')
        profile.last_name = self.cleaned_data.get('last_name')
        profile.phone_number = self.cleaned_data.get('phone_number')
        profile.street_address1 = self.cleaned_data.get('street_address1')
        profile.street_address2 = self.cleaned_data.get('street_address2')
        profile.town_city = self.cleaned_data.get('town_city')
        profile.county_state = self.cleaned_data.get('county_state')
        profile.postal_code = self.cleaned_data.get('postal_code')
        profile.country = self.cleaned_data.get('country')
        profile.save()

        return user