# yachtsescape/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('yachts/', include('yachts.urls')),
    path('booking/', include('booking.urls')),
    # path('profiles/', include('profiles.urls')),
    path('accounts/', include('allauth.urls')),
    path('checkout/', include('checkout.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)