# profiles/urls.py

from django.urls import path
from .views import profile, profile_edit

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]