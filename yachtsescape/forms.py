from allauth.account.forms import SignupForm
from django import forms
from profiles.models import UserProfile

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30,
        label="First Name",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
    )
    last_name = forms.CharField(
        max_length=30,
        label="Last Name",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
    )
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
    
    # Add custom password fields
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'id': 'password1'}),
        min_length=8,
        required=True,
        help_text="Password must contain at least 8 characters, including UPPERCASE letters and numbers.",
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'id': 'password2'}),
        required=True,
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        print("User created:", user)

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