from django.db import models
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
import logging
import os
import boto3  # Ensure you import boto3

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
    # Uploaded image of the yacht for the listing
    card_image = models.ImageField(upload_to='yachts/cards/', null=True, blank=True)
    # Uploaded images of the yacht for the details
    detail_image = models.ImageField(upload_to='yachts/details/', null=True, blank=True)
    # External URL for the detail image, if needed
    detail_image_url = models.URLField(max_length=1024, null=True, blank=True)

    def get_files_from_s3(self, folder_path):
        """Fetches all files from the specified S3 folder."""
        s3_client = boto3.client('s3')
        response = s3_client.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Prefix=folder_path)
        files = []
        if 'Contents' in response:
            for obj in response['Contents']:
                files.append(obj['Key'])
        return files

    def get_card_images(self):
        """Returns a list of URLs to the card images of the yacht."""
        card_images = []
        folder_path = os.path.join(settings.MEDIA_ROOT, 'yachts/cards')
        
        # Check local directory for images
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    card_images.append(f"/media/yachts/cards/{filename}")
        else:
            logger.warning("Card images folder does not exist.")

        return card_images

    def get_detail_images(self):
        detail_images = []
        
        if self.detail_image:
            detail_images.append(self.detail_image.url)

        if self.detail_image_url:
            detail_images.append(self.detail_image_url)

        folder_path = f'yachts/details/{self.id}/'
        s3_client = boto3.client('s3')
        try:
            response = s3_client.list_objects_v2(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Prefix=folder_path
            )
            if 'Contents' in response:
                for obj in response['Contents']:
                    image_url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{obj['Key']}"
                    detail_images.append(image_url)
        except Exception as e:
            logger.error(f"Error fetching images from S3: {e}")

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
        if self.card_image:  # Ensure card_image exists before trying to delete it
            storage = S3Boto3Storage()
            storage.delete(self.card_image.name)  # Delete the image from S3 storage
            logger.info(f"Image deleted from S3: {self.card_image.name}")  # Log successful deletion
        super().delete(*args, **kwargs)  # Delete the model instance

    def __str__(self):
        """Return the name of the yacht as its string representation."""
        return self.name  # String representation of the model