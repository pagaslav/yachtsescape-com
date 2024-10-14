# booking/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('booking/create/', views.booking_create, name='booking_create'),
]