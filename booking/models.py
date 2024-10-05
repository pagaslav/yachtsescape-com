# booking/models.py

from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    yacht = models.ForeignKey('yachts.Yacht', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.yacht.name} - {self.start_date} to {self.end_date}"