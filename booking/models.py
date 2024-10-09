# booking/models.py

from django.db import models
from yachts.models import Yacht  # Импорт модели Yacht
from django.utils import timezone

class Booking(models.Model):
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        # Calculate the total cost based on the yacht's daily rate and duration
        if self.start_date and self.end_date:
            num_days = (self.end_date - self.start_date).days
            if num_days > 0:
                self.total_cost = self.yacht.price_per_day * num_days
            else:
                self.total_cost = 0  # Или обработка ошибок
        super().save(*args, **kwargs)  # Сохранение объекта