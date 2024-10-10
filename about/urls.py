from django.urls import path
from . import views
from .views import AboutView

urlpatterns = [
    path('add_review/', views.add_review, name='add_review'),
    path('', AboutView.as_view(), name='about'),

]