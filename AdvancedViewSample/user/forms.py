from typing import Any
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    username = forms.CharField(label='Name', max_length=100)
    email =forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('name','email', 'password', 'confirm_password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Password doesn\'t match.')


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(label='website url')
    picture = forms.FileField(label='Choos file for your picture')

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')