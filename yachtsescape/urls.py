"""
yachtsescape/urls.py
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500, handler403, handler400

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('yachts/', include('yachts.urls')),
    path('booking/', include('booking.urls')),
    path('profiles/', include('profiles.urls')),
    path('accounts/', include('allauth.urls')),
    path('about/', include('about.urls')),
]

handler404 = 'home.views.handler404'
handler500 = 'home.views.handler500'
handler403 = 'home.views.handler403'
handler400 = 'home.views.handler400'

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
