from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('user_activate/<str:token>', views.user_activate, name='user_activate'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('edit', views.user_edit, name='edit'),
    path('password_edit', views.user_password_edit, name='password_edit'),
]