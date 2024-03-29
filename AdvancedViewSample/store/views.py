from django.shortcuts import render
from .models import Items

# Create your views here.

def item_list(request):
  items = Items.objects.all()
  return render(request, 'store/item_list.html', context={
    'items': items
  })

def item_detail(request, id):
  item = Items.objects.filter(id=id).get()
  return render(request, 'store/item_detail.html', context = {
      'item': item
  })