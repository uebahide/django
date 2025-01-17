from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('home', views.home, name='home'),
    path('regsiter', views.user_register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
]