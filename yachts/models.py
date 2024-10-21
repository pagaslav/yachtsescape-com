from django.db import models
from cloudinary.models import CloudinaryField
import logging

# Configure logging
logger = logging.getLogger(__name__)

class Yacht(models.Model):
    COUNTRY_CHOICES = [
        ('Turkey', 'Turkey'),
        ('France', 'France'),
        ('Spain', 'Spain'),
    ]

    # Yacht fields
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, default='default_type')
    description = models.TextField()
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default='Turkey')
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # Cloudinary image fields
    card_image = CloudinaryField('card image', folder='yachts/cards', null=True, blank=True)
    detail_image1 = CloudinaryField('detail image 1', folder='yachts/details', null=True, blank=True)
    detail_image2 = CloudinaryField('detail image 2', folder='yachts/details', null=True, blank=True)
    detail_image3 = CloudinaryField('detail image 3', folder='yachts/details', null=True, blank=True)

    def get_detail_images(self):
        """Returns a list of URLs of detail images."""
        return [
            self.detail_image1.url if self.detail_image1 else None,
            self.detail_image2.url if self.detail_image2 else None,
            self.detail_image3.url if self.detail_image3 else None
        ]

    def save(self, *args, **kwargs):
        """Override the save method to add logging."""
        try:
            logger.debug(f"Attempting to save yacht: {self.name}")
            logger.debug(f"Card Image: {self.card_image}")
            super().save(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error uploading image: {e}")
            raise

    def delete(self, *args, **kwargs):
        """Override the delete method to add logging."""
        try:
            logger.info(f"Attempting to delete yacht: {self.name}")
            super().delete(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error deleting yacht: {e}")
            raise

    def __str__(self):
        """Return the string representation of the yacht."""
        return self.name