from django.urls import path
from . import views

app_name = 'formapp'

urlpatterns = [
    path('index', views.index, name="index"),
    path('create', views.create, name="create"),
    path('create_set', views.create_set, name="create_set"),
    path('store', views.store, name="store"),
    path('store_set', views.store_set, name="store_set"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('destroy', views.destroy, name="destroy")
]