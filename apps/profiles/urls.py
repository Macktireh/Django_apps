from django.urls import path
from apps.profiles import views

urlpatterns = [
    path('<str:pseudo>', views.profile, name='profile'),
]