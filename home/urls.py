""" home/urls.py """

from django.urls import path
from home.views import test_403_error
from home.views import test_500_error
from home.views import test_400_error
from . import views


urlpatterns = [
    path('', views.home, name='home'),
]