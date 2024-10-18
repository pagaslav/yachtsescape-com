# # booking/signals.py
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from .models import Booking

# @receiver(post_save, sender=Booking)
# def update_booking_on_save(sender, instance, created, **kwargs):
#     """
#     Recalculate total cost on booking update/create.
#     """
#     if not created:  # If this is not a new booking
#         instance.save()  # Recalculate total_cost when the booking is updated

# @receiver(post_delete, sender=Booking)
# def update_booking_on_delete(sender, instance, **kwargs):
#     """
#     Actions to perform when a booking is deleted.
#     """
#     # Add any actions needed when a booking is deleted.
#     # For example, you could update yacht availability if required.