from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add(request, num1, num2):
  return HttpResponse(f'<h1>{num1 + num2}</h1>')

def minus(request, num1, num2):
  return HttpResponse(f'<h1>{num1-num2}</h1>')

def div(request, num1, num2):
  result = round(num1/num2);
  return HttpResponse(f'<h1>{result}</h1>')