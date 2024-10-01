from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),  # Existing path for home
    path('yachts/', views.yacht_list, name='yacht_list'),  # New path for yacht list
    path('yachts/<int:yacht_id>/', views.yacht_detail, name='yacht_detail'),  # New path for yacht detail
]