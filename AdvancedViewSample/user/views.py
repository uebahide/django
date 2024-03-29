from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserForm, UserProfileForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
# Create your views here.

def home(request):
  return render(request, 'user/home.html')

def register(request):
  user_form = UserForm(request.POST or None)
  profile_form = UserProfileForm(request.POST or None, request.FILES or None)
  if user_form.is_valid() and profile_form.is_valid():
    user = user_form.save(commit=False)
    try:
      validate_password(user_form.cleaned_data.get('password'), user)
    except ValidationError as e:
      user_form.add_error('password', e)
      return render(request, 'user/register.html', context={
        'user_form' : user_form,
        'profile_form': profile_form
      })
    user.set_password(user.password)
    user.save()
    profile = profile_form.save(commit=False)
    profile.user = user
    profile.save()
    return redirect('user:home')
  return render(request, 'user/register.html', context = {
    'user_form' : user_form,
    'profile_form': profile_form
  })