from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'index.html', context={'value': 'hello'})

def home(request):
  my_name = 'Taro Yamada'
  favorite_fruites = ['apple', 'grape', 'lemon']
  my_info = {
    'name': 'Taro',
    'age': 18
  }

  return render(request, 'home.html', context = {
    'my_name': my_name,
    'favorite_fruites': favorite_fruites,
    'my_info' : {
      'name': 'Taro',
      'age' : 18
    }
  })

def sample1(request):
  return render(request, 'sample1.html')
  