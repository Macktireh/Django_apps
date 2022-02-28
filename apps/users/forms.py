from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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
    first_name = forms.CharField(min_length=2, required=True, widget=forms.TextInput(attrs={'id': 'firstname', 'class': 'form-control', 'autocomplete': 'off'}))
    last_name = forms.CharField(min_length=2, required=True, widget=forms.TextInput(attrs={'id': 'lastname', 'class': 'form-control', 'autocomplete': 'off'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'autocomplete': 'off'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'form-control', 'autocomplete': 'off'}))
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'id': 'confirm', 'class': 'form-control', 'autocomplete': 'off'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']
        
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name is None:
            raise ValidationError('the first name must be at least 10 characters')
        elif len(first_name) < 3:
            raise ValidationError(f'first_name : the first name must be at least 10 characters ({first_name})')
        else:
            print('OK')
        return first_name
        

class Sign_InForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'autocomplete': 'off'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'form-control', 'autocomplete': 'off'}))
    
    class Meta:
        model = User
        fields = ['email', 'password']