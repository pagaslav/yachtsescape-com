# booking/models.py

from django.db import models
from yachts.models import Yacht  # Import the Yacht model
from django.utils import timezone

class Booking(models.Model):
    # ForeignKey to link each booking to a specific yacht
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE, related_name='bookings')
    # Start and end dates for the booking
    start_date = models.DateField()
    end_date = models.DateField()
    # Total cost for the booking, calculated based on the yacht's daily rate
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # Status field to track the current state of the booking
    status = models.CharField(
        max_length=20, 
        choices=[
            ('pending', 'Pending'),  # Initial status, awaiting confirmation
            ('confirmed', 'Confirmed'),  # Status when payment is successful
            ('cancelled', 'Cancelled')  # Status when the booking is cancelled
        ], 
        default='pending'  # Default to 'pending' until payment is confirmed
    )
    # Timestamp for when the booking was created
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to calculate the total cost
        based on the yacht's daily rate and the number of days booked.
        """
        if self.start_date and self.end_date:
            # Calculate the number of days for the booking
            num_days = (self.end_date - self.start_date).days
            if num_days > 0:
                # Set the total cost based on the daily rate and the booking duration
                self.total_cost = self.yacht.price_per_day * num_days
            else:
                # Set the total cost to 0 if dates are invalid (negative duration)
                self.total_cost = 0
        # Save the booking instance
        super().save(*args, **kwargs)

    def confirm_booking(self):
        """
        Method to confirm the booking by setting its status to 'confirmed'.
        This should be called after successful payment.
        """
        self.status = 'confirmed'
        self.save()

    def cancel_booking(self):
        """
        Method to cancel the booking by setting its status to 'cancelled'.
        This can be used if the payment fails or the user cancels the booking.
        """
        self.status = 'cancelled'
        self.save()