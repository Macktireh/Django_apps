from django.urls import path
from apps.accounts import views


urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sing_in, name='sign_in'),
    path('logout/', views.user_logout, name='logout'),
]