# yachts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.yacht_list, name='yacht_list'),  # URL для страницы списка яхт
]