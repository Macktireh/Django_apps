
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('apps.home.urls')),
    path('accounts/', include('apps.users.urls')),
    path('in/', include('apps.profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
