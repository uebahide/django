from typing import Any
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Password confirmatio', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
          raise ValidationError('Password does not match!')

    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'website', 'picture', 'is_active', 'is_staff', 'is_superuser')


    def clean_password(self):
        return self.initial['password']