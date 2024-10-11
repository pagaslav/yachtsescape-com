# about/urls.py

from django.urls import path
from .views import AboutView

urlpatterns = [
    path('', AboutView.as_view(), name='about'),  # Route for the About page
    # path('review/<int:review_id>/helpful/', mark_helpful, name='mark_helpful'),
    # path('review/<int:review_id>/report/', report_review, name='report_review'),
]