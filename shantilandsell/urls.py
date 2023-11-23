# your_project/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landapp.urls')),
    path('contact/', include('contact.urls')),
    path('abouts/', include('abouts.urls')),
    path('service/', include('service.urls')),
    path('accounts/', include('accounts.urls')),
    path('search/', include('search.urls')),
    path('message/', include('inquiry.urls')),
    # Include your app URLs here
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
