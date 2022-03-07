from django.urls import path
from apps.home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pro/', views.home1, name='home1'),
]