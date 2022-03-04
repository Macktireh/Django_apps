from django.urls import path
from django.contrib.auth import views
from apps.users.views import sign_up, sign_in, user_logout, activated_confirm_eamil_token


urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('logout/', user_logout, name='logout'),
    path('activate/<uidb64>/<token>', activated_confirm_eamil_token, name='activate'),
    
    path('reset_password', views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='reset_password'),
    path('reset_password_send', views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(template_name='users/password_reset_send.html'), name='password_reset_complete')    
]