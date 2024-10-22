"""
yachts/models.py
"""

from django.db import models
from cloudinary.models import CloudinaryField


class Yacht(models.Model):
    """ Model representing a Yacht with various attributes """
    COUNTRY_CHOICES = [
        ('Turkey', 'Turkey'),
        ('France', 'France'),
        ('Spain', 'Spain'),
    ]
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, default='default_type')
    description = models.TextField()
    country = models.CharField(
        max_length=50, choices=COUNTRY_CHOICES, default='Turkey'
    )
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )

    card_image = CloudinaryField(
        'image', folder='yachts/cards', null=True, blank=True
    )
    detail_image1 = CloudinaryField(
        'image', folder='yachts/details', null=True, blank=True
    )
    detail_image2 = CloudinaryField(
        'image', folder='yachts/details', null=True, blank=True
    )
    detail_image3 = CloudinaryField(
        'image', folder='yachts/details', null=True, blank=True
    )

    def get_card_images(self):
        """ Returns card image URL if available """
        card_images = []
        if self.card_image:
            card_images.append(self.card_image.url)
        return card_images

    def get_detail_images(self):
        """ Returns a list of detail image URLs if available """
        return [
            image.url for image in [
                self.detail_image1, self.detail_image2, self.detail_image3
            ] if image
        ]

    def save(self, *args, **kwargs):
        """ Overrides save method """
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """ Overrides delete method """
        super().delete(*args, **kwargs)

    def __str__(self):
        """ String representation of the Yacht model """
        return self.name
