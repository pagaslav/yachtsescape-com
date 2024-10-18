# about/models.py

from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    rating = models.PositiveIntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        # String representation of the review
        user_display = self.user.username if self.user else 'Anonymous'
        return f"{user_display} - {self.rating}"