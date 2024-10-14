# checkout/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<int:booking_id>/<str:start_date>/<str:end_date>/', views.checkout, name='checkout'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/<order_number>/', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('webhook/', views.webhook, name='webhook'),
]