""" profiles/models.py """

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    street_address1 = models.CharField(max_length=255, blank=False, null=False)
    street_address2 = models.CharField(max_length=255, blank=True, null=True)
    town_city = models.CharField(max_length=50, blank=False, null=False)
    county_state = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f"{self.user.username}'s Profile"
