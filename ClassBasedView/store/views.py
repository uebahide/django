from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import BookForm
from .models import BookModel
from django.views.generic.base import (
  View, TemplateView
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView, DeleteView

# Create your views here.

class IndexView(View, SuccessMessageMixin):

  def get(self, request, *args, **kwargs):
    book_form = BookForm()
    return render(request, 'book/index.html', context={
      'form': book_form
    })
  
  def post(self, request, *args, **kwargs):
    book_form = BookForm(request.POST or None)
    if book_form.is_valid():
      book_form.save()
      messages.info(request, 'New book was created successfully.')
      return redirect('store:index')
    return render(request, 'book/index.html', context={
      'form': book_form
    })
  

class BookTemplateView(TemplateView):
    template_name = 'book/book_index.html'

class BookDetailView(DetailView):
    model = BookModel
    template_name = 'book/book_detail.html'

class BookListView(ListView):
    model = BookModel
    template_name = 'book/book_list.html'

class BookCreateView(SuccessMessageMixin, CreateView):
    model = BookModel
    template_name = 'book/book_create.html'
    form_class = BookForm
    success_message = 'New book was create successfully.'
  
    def get_initial(self, **kwargs):
      initial = super(BookCreateView, self).get_initial(**kwargs)
      initial['title'] = 'sample'
      initial['description'] = 'sample description'
      initial['price'] = 100
      return initial


class BookUpdateView(SuccessMessageMixin, UpdateView):
    model = BookModel
    template_name = 'book/book_update.html'
    form_class = BookForm
    success_message = 'Book was updated successfully.'

    def get_context_data(self, **kwargs):
        context = super(BookUpdateView, self).get_context_data(**kwargs)
        return context
    

class BookDeleteView(SuccessMessageMixin ,DeleteView):
    model = BookModel
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('store:book_list')
    success_message = 'Book was deleted successfully.'