# about/models.py

from django.db import models
from django.contrib.auth.models import User  # Import the default User model

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model; deletes review if user is deleted
    content = models.TextField()  # Field for the review text
    rating = models.PositiveIntegerField()  # Field for the rating, for example, 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)  # Field for the creation date; set automatically on creation

    def __str__(self):
        # String representation of the review
        return f"Review by {self.user.username} - Rating: {self.rating}"