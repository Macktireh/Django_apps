from django.urls import path
from django.contrib.auth import views
from apps.users.views import sign_up, sign_in, user_logout


urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('logout/', user_logout, name='logout'),
    
    path('reset_password', views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='reset_password'),
    path('reset_password_send', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(), name='password_reset_complete')    
]