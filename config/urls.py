
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('apps.home.urls')),
    path('accounts/', include('apps.users.urls')),
    path('profiles', include('apps.profiles.urls')),
]
