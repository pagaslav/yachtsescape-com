from django.urls import path
from . import views

urlpatterns = [
    path('', views.yacht_list, name='yacht_list'),  # URL для страницы списка яхт
    path('yacht/<int:yacht_id>/', views.yacht_detail, name='yacht_detail'),  # URL для страницы с деталями яхты
]