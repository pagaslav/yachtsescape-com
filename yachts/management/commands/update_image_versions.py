import os
from django.core.management.base import BaseCommand
from yachts.models import Yacht
import logging

# Configure logging
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Update image URLs in the Yacht model from Cloudinary.'

    def handle(self, *args, **kwargs):
        # Base URL for Cloudinary
        cloudinary_base_url = 'https://res.cloudinary.com/da57wfabx/image/upload'
        version = 'v1729523432'  # Replace with your desired version

        # Define the yacht images dictionary
        yacht_images = {
            3: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-3-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/3/yacht-3-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/3/yacht-3-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/3/yacht-3-detail-3.webp',
                ]
            },
            4: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-4-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/4/yacht-4-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/4/yacht-4-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/4/yacht-4-detail-3.webp',
                ]
            },
            5: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-5-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/5/yacht-5-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/5/yacht-5-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/5/yacht-5-detail-3.webp',
                ]
            },
            6: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-6-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/6/yacht-6-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/6/yacht-6-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/6/yacht-6-detail-3.webp',
                ]
            },
            7: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-7-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/7/yacht-7-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/7/yacht-7-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/7/yacht-7-detail-3.webp',
                ]
            },
            8: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-8-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/8/yacht-8-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/8/yacht-8-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/8/yacht-8-detail-3.webp',
                ]
            },
            9: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-9-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/9/yacht-9-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/9/yacht-9-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/9/yacht-9-detail-3.webp',
                ]
            },
            10: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-10-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/10/yacht-10-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/10/yacht-10-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/10/yacht-10-detail-3.webp',
                ]
            },
            11: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-11-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/11/yacht-11-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/11/yacht-11-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/11/yacht-11-detail-3.webp',
                ]
            },
            12: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-12-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/12/yacht-12-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/12/yacht-12-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/12/yacht-12-detail-3.webp',
                ]
            },
            13: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-13-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/13/yacht-13-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/13/yacht-13-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/13/yacht-13-detail-3.webp',
                ]
            },
            14: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-14-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/14/yacht-14-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/14/yacht-14-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/14/yacht-14-detail-3.webp',
                ]
            },
            15: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-15-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/15/yacht-15-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/15/yacht-15-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/15/yacht-15-detail-3.webp',
                ]
            },
            16: {
                'card_image': f'{cloudinary_base_url}/{version}/yachts/cards/yacht-16-card.webp',
                'detail_images': [
                    f'{cloudinary_base_url}/{version}/yachts/details/16/yacht-16-detail-1.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/16/yacht-16-detail-2.webp',
                    f'{cloudinary_base_url}/{version}/yachts/details/16/yacht-16-detail-3.webp',
                ]
            },
        }

        # Update each yacht object with the new URLs
        for yacht_id, images in yacht_images.items():
            try:
                yacht = Yacht.objects.get(id=yacht_id)
                yacht.card_image = images['card_image']
                yacht.detail_image1 = images['detail_images'][0]
                yacht.detail_image2 = images['detail_images'][1]
                yacht.detail_image3 = images['detail_images'][2]
                yacht.save()
                logger.info(f"Updated yacht {yacht.name} with new image URLs.")
            except Yacht.DoesNotExist:
                logger.error(f"Yacht with ID {yacht_id} does not exist.")
            except Exception as e:
                logger.error(f"Error updating yacht {yacht_id}: {str(e)}")

        self.stdout.write(self.style.SUCCESS('Successfully updated all yacht image URLs.'))