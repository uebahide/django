from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import Student, School

from .forms import UserChangeForm, UserCreateForm

User = get_user_model()


# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ['username', 'email', 'is_staff']

    fieldsets = [
        ('Personal info', {'fields' : ['username', 'email', 'password', 'website', 'picture']}),
        ('Permission', {'fields' : ['is_active', 'is_staff', 'is_superuser']}),
    ]

    add_fieldsets = [
        ('Personal info', {'fields': ['username', 'email', 'password', 'confirm_password']})
    ]



admin.site.register(User, UserAdmin)
# admin.site.register(Student)
admin.site.register(School)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('name', 'age', 'score', 'school')
    list_display = ('id', 'name', 'age', 'score', 'school')
    ordering = ['score', 'id']
    list_display_links = ['name']

    
