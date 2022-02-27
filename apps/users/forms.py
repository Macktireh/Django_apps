from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from apps.users.models import CustomUser

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
        

class Sign_UpForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, min_length=2, required=True, widget=forms.TextInput(attrs={'id': 'firstname', 'class': 'form-control', 'autocomplete': 'off'}))
    last_name = forms.CharField(max_length=50, min_length=2, required=True, widget=forms.TextInput(attrs={'id': 'lastname', 'class': 'form-control', 'autocomplete': 'off'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'autocomplete': 'off'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'form-control', 'autocomplete': 'off'}))
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'id': 'confirm', 'class': 'form-control', 'autocomplete': 'off'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']
        

class Sign_InForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'autocomplete': 'off'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'form-control', 'autocomplete': 'off'}))
    
    class Meta:
        model = User
        fields = ['email', 'password']