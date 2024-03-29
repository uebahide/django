from django.shortcuts import render, redirect
from django.http import HttpResponse
from .froms import UserForm, UserProfileForm, LoginForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
  return render(request, 'user/home.html')

def user_register(request):
  user_form = UserForm(request.POST or None)
  profile_form = UserProfileForm(request.POST or None, request.FILES or None)
  if user_form.is_valid() and profile_form.is_valid():
    user = user_form.save(commit=False)
    try:
      validate_password(user_form.cleaned_data.get('password'), user)
    except ValidationError as e:
      user_form.add_error('password', e)
      return render(request, 'user/register.html', context = {
        'user_form': user_form,
        'profile_form': profile_form
      })
    user.set_password(user.password)
    user.save()
    profile = profile_form.save(commit=False)
    profile.user = user
    profile.save()
    return redirect('user:home')
  return render(request, 'user/register.html', context = {
      'user_form': user_form,
      'profile_form': profile_form
  })

def user_login(request):
  form = LoginForm(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      if user.is_active:
        login(request, user)
        return redirect('user:home')
      else:
        return HttpResponse('This account is not active.')
    else:
      form.add_error(None, 'User name or password is wrong.')
  return render(request, 'user/login.html', context ={
    'form': form
  })

@login_required
def user_logout(request):
  logout(request)
  return redirect('user:home')