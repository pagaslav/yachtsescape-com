# home/models.py
from django.db import models

# Model representing a yacht
class Yacht(models.Model):
    name = models.CharField(max_length=100)  # Name of the yacht
    description = models.TextField()  # Description of the yacht
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per day for rental