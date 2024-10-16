# checkout/models.py

import uuid
from django.db import models
from django_countries.fields import CountryField
from booking.models import Booking
from profiles.models import UserProfile  # Make sure this model is accessible

class Order(models.Model):
    # ForeignKey linking to the user's profile, allowing order history access
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='orders'
    )
    # One-to-One relationship with the Booking model
    booking = models.OneToOneField(
        Booking, on_delete=models.CASCADE, related_name='order'
    )
    
    # Order contact information
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, blank=True, null=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    county = models.CharField(max_length=80, blank=True, null=True)
    
    # Payment and order tracking information
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    
    # Order status and timestamp
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=[
            ('pending', 'Pending'),      # Order is created but not yet paid
            ('processing', 'Processing'), # Payment is in process
            ('complete', 'Complete'),     # Payment is successful, and order is confirmed
            ('cancelled', 'Cancelled'),   # Order is cancelled or payment failed
        ],
        default='pending'
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID for tracking purposes.
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to:
        - Set the order number if it hasn't been set already.
        - Assign the booking's total_cost to the order total cost field.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        # Assign total cost from the associated booking
        self.total_cost = self.booking.total_cost
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number