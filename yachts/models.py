# yachts/models.py

from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
import logging
import os

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
    # Uploaded image of the yacht
    image = models.ImageField(upload_to='yachts/cards/', null=True, blank=True)
    # New field for detailed images
    detail_image = models.ImageField(upload_to='yachts/details/', null=True, blank=True)

    def get_detail_images(self):
        """Returns a list of URLs to the detailed images of the yacht."""
        detail_images = []
        # Folder path based on yacht ID (no leading zeros)
        folder_path = f"yachts/details/{self.id}"
        
        # Check if using S3 storage
        if 'AWS_STORAGE_BUCKET_NAME' in os.environ:
            # Base URL for accessing images from S3 bucket
            s3_base_url = f"https://{os.environ['AWS_STORAGE_BUCKET_NAME']}.s3.amazonaws.com/"
            for num in range(1, 4):  # Adjust the range to match your images count per yacht
                image_url = f"{s3_base_url}{folder_path}/yacht-{self.id}-detail-{num}.webp"
                detail_images.append(image_url)
                logger.debug(f"Adding S3 image URL to list: {image_url}")
        else:
            # Local development path
            media_base_url = "/media/"
            if os.path.exists(media_base_url + folder_path):
                for filename in os.listdir(media_base_url + folder_path):
                    if filename.endswith(('.png', '.jpg', '.jpeg', '.webp')):
                        image_url = f"{media_base_url}{folder_path}/{filename}"
                        detail_images.append(image_url)
                        logger.debug(f"Adding local image URL to list: {image_url}")
            else:
                logger.warning(f"Folder {media_base_url + folder_path} does not exist for yacht ID {self.id}")

        return detail_images

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