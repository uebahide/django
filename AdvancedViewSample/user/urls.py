from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('home', views.home, name='home'),
    path('register', views.register , name='register'),
]