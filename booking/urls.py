from django.urls import path
from . import views

urlpatterns = [
    path('booking/create/', views.booking_create, name='booking_create'),
    path('booking_success/<int:booking_id>/', views.booking_success, name='booking_success'),
]