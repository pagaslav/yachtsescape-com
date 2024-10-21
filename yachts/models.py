from django.db import models
import os
from cloudinary.models import CloudinaryField
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class Yacht(models.Model):
    COUNTRY_CHOICES = [
        ('Turkey', 'Turkey'),
        ('France', 'France'),
        ('Spain', 'Spain'),
    ]
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, default='default_type')
    description = models.TextField()
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default='Turkey')
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    available = models.BooleanField(default=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    # Используем разные поля в зависимости от значения DEBUG
    if settings.DEBUG:
        # Для локальной разработки используем ImageField
        card_image = models.ImageField(upload_to='yachts/cards/', null=True, blank=True)
        detail_image = models.ImageField(upload_to='yachts/details/', null=True, blank=True)
    else:
        # В продакшн используем CloudinaryField
        card_image = CloudinaryField('image', folder='yachts/cards', null=True, blank=True)
        detail_image = CloudinaryField('image', folder='yachts/details', null=True, blank=True)

    detail_image_url = models.URLField(max_length=1024, null=True, blank=True)

    def get_card_images(self):
        card_images = []
        if self.card_image:
            logger.debug(f"Card image URL: {self.card_image.url}")
            card_images.append(self.card_image.url)
        else:
            logger.warning("No card image available for this yacht.")
        return card_images

    def get_detail_images(self):
        """Retrieve all images stored in the 'media/yachts/details/{yacht_id}' directory."""
        detail_images = []
        yacht_directory = os.path.join(settings.MEDIA_ROOT, 'yachts', 'details', str(self.id))

        # Check if the directory exists
        if os.path.exists(yacht_directory):
            # List all files in the directory
            for image_file in os.listdir(yacht_directory):
                # Construct the URL for each image file
                image_url = os.path.join(settings.MEDIA_URL, 'yachts', 'details', str(self.id), image_file)
                detail_images.append(image_url)
                logger.debug(f"Detail image URL: {image_url}")
        else:
            logger.warning(f"Yacht images directory not found for yacht {self.id}: {yacht_directory}")
        
        return detail_images

    def save(self, *args, **kwargs):
        try:
            logger.debug(f"Attempting to save yacht: {self.name}")
            super().save(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error uploading image: {e}")
            raise

    def delete(self, *args, **kwargs):
        try:
            logger.info(f"Attempting to delete yacht: {self.name}")
            super().delete(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error deleting yacht: {e}")
            raise

    def __str__(self):
        return self.name