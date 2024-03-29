from django.urls import path
from . import views

app_name = 'FirstApp'

urlpatterns = [
  path('add/<int:num1>/<int:num2>', views.add, name = 'add'),
  path('minus/<int:num1>/<int:num2>', views.minus, name = 'minus'),
  path('div/<int:num1>/<int:num2>', views.div, name = 'div'),
]