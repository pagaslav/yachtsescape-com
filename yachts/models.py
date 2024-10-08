# yachts/models.py

from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
import logging

# Setting up logging for error tracking
logger = logging.getLogger(__name__)

class Yacht(models.Model):
    COUNTRY_CHOICES = [
        ('Turkey', 'Turkey'),
        ('France', 'France'),
        ('Spain', 'Spain'),
    ]
    # Name of the yacht
    name = models.CharField(max_length=100)  
    # ID for inventory management
    id = models.AutoField(primary_key=True)
    # Type of yacht (e.g., sailing, motor)
    type = models.CharField(max_length=50, default='default_type')
    # Detailed description of the yacht
    description = models.TextField()
    # Country where the yacht is available
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default='Turkey')
    # Location where the yacht is available
    location = models.CharField(max_length=100)
    # Maximum number of people the yacht can accommodate
    capacity = models.IntegerField()
    # Price per day for renting the yacht
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    # Optional rating for the yacht
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    # Availability status of the yacht
    available = models.BooleanField(default=True)
    # URL for an external image of the yacht
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    # Uploaded image of the yacht upload_to='yachts/cards/',
    image = models.ImageField(upload_to='yachts/cards/', null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Save the yacht instance to the database.
        Logs the image upload status.
        """
        try:
            logger.debug(f"Attempting to save yacht: {self.name}")  # Log the attempt to save
            super().save(*args, **kwargs)  # Save the model instance
            logger.info(f"Image uploaded successfully: {self.image.url}")  # Log successful upload
        except Exception as e:
            logger.error(f"Error uploading image: {e}")  # Log the error for debugging
            raise  # Raise the exception to prevent silent failure

    def delete(self, *args, **kwargs):
        """
        Delete the yacht instance from the database and remove the image from S3 storage if it exists.
        """
        if self.image:
            storage = S3Boto3Storage()
            storage.delete(self.image.name)  # Delete the image from S3 storage
            logger.info(f"Image deleted from S3: {self.image.name}")  # Log successful deletion
        super().delete(*args, **kwargs)  # Delete the model instance

    def __str__(self):
        """Return the name of the yacht as its string representation."""
        return self.name  # String representation of the model