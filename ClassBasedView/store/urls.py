from django.urls import path
from .views import (
  IndexView, BookTemplateView, BookDetailView, BookListView, BookCreateView, BookUpdateView, BookDeleteView
)

app_name = 'store'

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('book_index/', BookTemplateView.as_view(), name='book_index'),
    path('book_detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book_update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('book_create/', BookCreateView.as_view(), name='book_create'),
]