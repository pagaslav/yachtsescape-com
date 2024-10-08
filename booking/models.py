# booking/models.py

from django.db import models
from yachts.models import Yacht  # Импорт модели Yacht

class Booking(models.Model):
    YACHT_TYPES = [
        ('leisure', 'Leisure'),
        ('celebrations', 'Celebrations'),
        ('fishing', 'Fishing'),
    ]

    CAPACITY_CHOICES = [
        ('2-4', 'Up to 4'),
        ('4-6', '4-6'),
        ('6-8', '6-8'),
        ('8+', 'More than 8'),
    ]

    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE, related_name='bookings')  # Связь с моделью Yacht
    yacht_type = models.CharField(max_length=20, choices=YACHT_TYPES)  # Тип яхты
    capacity = models.CharField(max_length=5, choices=CAPACITY_CHOICES)  # Вместимость
    start_date = models.DateField()  # Дата начала аренды
    end_date = models.DateField()    # Дата окончания аренды

    def __str__(self):
        return f"{self.yacht_type.capitalize()} - {self.start_date} to {self.end_date}"