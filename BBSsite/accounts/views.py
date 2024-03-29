from django.shortcuts import render, redirect
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from .forms import UserRegisterForm, UserLoginForm, UserEditForm, UserPasswordEditForm
from .models import User, UserActivateToken


# Create your views here.

def home(request):
  return render(request, 'accounts/home.html')

def register(request):
  register_form = UserRegisterForm(request.POST or None)
  if register_form.is_valid():
    username = register_form.cleaned_data['username']
    email = register_form.cleaned_data['email']
    password = register_form.cleaned_data['password']
    user = User(
      username = username,
      email = email
    )
    try:
      validate_password(password, user)
      user.set_password(password)
      user.save()
      return redirect('accounts:home')
    except ValidationError as e:
      register_form.add_error('password', e)

  return render(request, 'accounts/register.html', context={
    'form': register_form
  })

def user_activate(request, token):
  UserActivateToken.objects.activate_user_by_token(token)
  return render(request, 'accounts/user_activate.html')

def user_edit(request):
  form = UserEditForm(request.POST or None, request.FILES or None, instance=request.user)
  if form.is_valid():
    messages.info(request, 'User profile was changed successfully.')
    form.save()
  url = ''
  if request.user.picture:
    url = request.user.picture.url
  
  return render(request, 'accounts/edit.html', context={
    'form': form,
    'url': url
  })

def user_password_edit(request):
  form = UserPasswordEditForm(request.POST or None, instance=request.user)
  if form.is_valid():
    try:
      user = form.save(commit=False)
      validate_password(form.cleaned_data.get('password'))
      user.set_password(user.password)
      user.save()
      update_session_auth_hash(request, request.user)
      messages.info(request, 'Password was changed successfully.')
    except ValidationError as e:
      form.add_error('password', e)
  
  return render(request, 'accounts/passwordEdit.html', context={
    'form': form
  })

def user_login(request):
  form = UserLoginForm(request.POST or None)
  if form.is_valid():
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']
    user = authenticate(request, email=email, password=password)
    if user:
      login(request, user)
      messages.info(request, "You are logged in successfully.")
      return redirect('accounts:home')

    else:
      messages.warning(request, 'Email or password is wrong.')
      messages.warning(request, 'Or')
      messages.warning(request, 'This user is not existing or is not active.')

  return render(request, 'accounts/login.html', context = {
    'form': form
  })

@login_required
def user_logout(request):
  logout(request)
  messages.info(request, 'You are logged out successfully.')
  return redirect('accounts:home')

