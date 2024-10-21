# home/urls.py

from django.urls import path

from home.views import test_403_error  # Импортируем представление для тестирования
from home.views import test_500_error  # Импортируем представление для тестирования
from home.views import test_400_error  # Импортируем представление для тестирования


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test-500/', test_500_error, name='test_500_error'),
    path('test-403/', test_403_error, name='test_403_error'),
    path('test-400/', test_400_error, name='test_400_error'),
]