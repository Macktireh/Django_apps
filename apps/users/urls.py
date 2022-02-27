from django.urls import path
from apps.users.views import sign_up, sign_in, user_logout


urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('logout/', user_logout, name='logout'),
]