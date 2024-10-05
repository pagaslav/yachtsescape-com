# booking/urls.py

from django.urls import path
from .views import yacht_detail

urlpatterns = [
    path('yacht/<int:yacht_id>/', yacht_detail, name='yacht_detail'),  # URL for yacht details
]