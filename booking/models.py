# booking/models.py

from django.db import models
from django.contrib.auth.models import User  # Import the User model
from yachts.models import Yacht  # Import the Yacht model
from django.utils import timezone

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')  # Add user field
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('cancelled', 'Cancelled')
        ],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_pid = models.CharField(max_length=254, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to calculate the total cost
        based on the yacht's daily rate and the number of days booked.
        """
        if self.start_date and self.end_date:
            # Calculate the number of days for the booking
            num_days = (self.end_date - self.start_date).days + 1
            
            # If the start date and end date are the same, count as one day
            if num_days == 0:
                num_days = 1  # Treat as one full day if booking is for a single day
            
            # Set the total cost based on the daily rate and the number of days booked
            self.total_cost = self.yacht.price_per_day * num_days
        else:
            # Set the total cost to 0 if dates are invalid (negative duration)
            self.total_cost = 0

        # Save the booking instance
        super().save(*args, **kwargs)

    def confirm_booking(self):
        self.status = 'confirmed'
        super().save(update_fields=['status'])  # Save only the 'status' field

    def cancel_booking(self):
        self.status = 'cancelled'
        self.save()
        super().save(update_fields=['status'])  # Save only the 'status' field