# booking/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('booking/create/', views.booking_create, name='booking_create'),
    path('yacht/<int:yacht_id>/', views.yacht_detail, name='yacht_detail'),
]