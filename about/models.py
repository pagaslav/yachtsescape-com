# about/models.py

from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()  # Field for the review text
    rating = models.PositiveIntegerField()  # Field for the rating, for example, 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)  # Field for the creation date; set automatically on creation
    # helpful_count = models.PositiveIntegerField(default=0)
    # helpful_users = models.ManyToManyField(User, related_name="helpful_reviews", blank=True)

    # reported = models.BooleanField(default=False)

    def __str__(self):
        # String representation of the review
        user_display = self.user.username if self.user else 'Anonymous'
        return f"{user_display} - {self.rating}"