from django.shortcuts import render
from ModelApp.models import Student
# Create your views here.

def home(request):
  studnet1 = Student.objects.filter(id=1).get()

  return render(request, 'Home.html', context={
    "student1": studnet1
  })


