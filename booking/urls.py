from django.urls import path
from . import views, webhooks

urlpatterns = [
    path('booking/create/', views.booking_create, name='booking_create'),
    path('booking_success/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('webhook/', webhooks.webhook, name='stripe_webhook'),
]