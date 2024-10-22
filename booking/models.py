""" booking/models.py """

from django.db import models
from django.contrib.auth.models import User
from yachts.models import Yacht
from django.db import transaction
import logging

logger = logging.getLogger(__name__)


class Booking(models.Model):
    """ Model representing a booking made for a yacht by a user """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings'
    )
    yacht = models.ForeignKey(
        Yacht, on_delete=models.CASCADE, related_name='bookings'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
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
        """ Override save to calculate the total cost of the booking """

        if self.start_date and self.end_date:
            num_days = (self.end_date - self.start_date).days + 1
            if num_days == 0:
                num_days = 1
            self.total_cost = self.yacht.price_per_day * num_days
        else:
            self.total_cost = 0

        super().save(*args, **kwargs)

    def confirm_booking(self):
        """ Confirm the booking and update its status """

        try:
            with transaction.atomic():
                self.status = 'confirmed'
                super().save(update_fields=['status'])
        except Exception as e:
            logger.error(f"Error confirming booking {self.id}: {e}")
            raise

    def cancel_booking(self):
        """ Cancel the booking and update its status """

        self.status = 'cancelled'
        super().save(update_fields=['status'])
