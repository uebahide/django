from typing import Any
from django import forms
from django.forms import TextInput, EmailInput, PasswordInput
from django.core.exceptions import ValidationError
from .models import User

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(
        label='User name', 
        max_length=120, 
        widget=forms.TextInput(
            attrs={
                'class': "border rounded-lg", 'placeholder': 'Name'
                }))
    email = forms.EmailField(
        label='Email', 
        widget=forms.EmailInput(
            attrs={
                'class': "border rounded-lg", 'placeholder': 'Email'
                }))
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(
            attrs={
                'class': "border rounded-lg", 'placeholder': 'minimum 9 characters'
                }))
    confirm_password = forms.CharField(
        label='Password confirmation', 
        widget=forms.PasswordInput(
            attrs={
                'class': "border rounded-lg", 'placeholder': 'confirm password'
                }))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('Password does not match!')


    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')



class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                 'class': "border rounded-lg", 
                 'placeholder': 'Email'
            }
        )
    )
    password = forms.CharField(
        label = 'Password',
        widget=forms.PasswordInput(
            attrs={
                'class': "border rounded-lg", 
                'placeholder': 'Password'
            }
        )
    )

class UserEditForm(forms.ModelForm):
    username = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'border rounded-lg'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'border rounded-lg'
            }
        )
    )
    picture = forms.FileField(
        required=False,
        label='Picture'
        )


    class Meta:
        model = User
        fields = ('username', 'email', 'picture') 

class UserPasswordEditForm(forms.ModelForm):
    password = forms.CharField(
        label='Password', 
        widget=PasswordInput(
            attrs={
                'class' : "rounded-lg border"
            }
        )
    )
    confirm_password = forms.CharField(
        label='Password confirmation',
        widget=PasswordInput(
            attrs={
                'class':'border rounded-lg'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Password does not match.')

    class Meta:
        model = User
        fields = ('password', 'confirm_password')