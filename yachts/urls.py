from django.urls import path
from . import views
from .views import YachtImageView

urlpatterns = [
    path('', views.yacht_list, name='yacht_list'),  # URL для страницы списка яхт
    path('yacht/<int:yacht_id>/', views.yacht_detail, name='yacht_detail'),  # URL для страницы с деталями яхты
    path('yacht/<int:yacht_id>/bookings/', views.yacht_booking_dates, name='bookings'),
    path('api/yacht/<int:yacht_id>/images/', YachtImageView.as_view(), name='yacht_images'),
]