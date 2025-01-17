from django.urls import path
from . import views

app_name = "template_app"

urlpatterns = [
    path('home', views.home, name="home"),
    path('members', views.members, name="members"),
    path('member_details/<int:id>', views.member_details, name="member_details"),
]