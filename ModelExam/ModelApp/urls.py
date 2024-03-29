from django.urls import path
from . import views

app_name = 'ModelApp'

urlpatterns = [
    path('home/<int:sid>', views.home, name='home')
]