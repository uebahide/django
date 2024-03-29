from typing import Any
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    username = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email', 'password', 'confirm_password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
          raise ValidationError('Password does not match!')

class UserProfileForm(forms.ModelForm):
    website = forms.URLField(label='Website URL')
    picture = forms.FileField(label='Picture')

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class LoginForm(forms.Form):
    username = forms.CharField(label='Name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())