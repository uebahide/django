from django.shortcuts import render, redirect, get_object_or_404
from FormApp.forms import StudentForm
from .models import Student
from django.forms import modelformset_factory

# Create your views here.

def index(request):
  students = Student.objects.all()
  return render(request, 'students/index.html', context={
    'students': students
  })

def create(request):
  form = StudentForm()
  return render(request, 'students/create.html', context={
    'form': form
  })

def create_set(request):
  empty_queryset = Student.objects.none()
  studentFormset = modelformset_factory(Student, form=StudentForm, extra=3)
  formset = studentFormset(queryset=empty_queryset)

  return render(request, 'students/create_set.html', context = {
    'formset': formset
  })

def store_set(request):
  if request.method == 'POST':
    studentFormSet = modelformset_factory(Student, StudentForm, extra=3)
    formset = studentFormSet(request.POST, request.FILES)
    if formset.is_valid():
      formset.save()
      return redirect('formapp:index')
      
  else:
    formset = studentFormSet(queryset=Student.objects.none())

  return render(request, 'students/create_set.html', context = {
    'formset': formset
  })

def store(request):
  if request.method == 'POST':
    form = StudentForm(request.POST, request.FILES)
    if form.is_valid():    
      form.save()
      return redirect("formapp:index")

  else:
    form = StudentForm()

  return render(request, 'students/create.html', context={
    'form': form
  })


def edit(request, id):
  student = get_object_or_404(Student, id=id)
  form = StudentForm(instance=student)
  return render(request, 'students/edit.html', context={
    'form': form,
    'id': id
  })

def update(request, id):
  student = get_object_or_404(Student, id=id)
  if request.method == 'POST':
    form = StudentForm(request.POST, request.FILES, instance=student)
    if form.is_valid():
      form.save()
      return redirect('formapp:index')
    
  else:
    form = StudentForm(instance=student)

  return render(request, 'students/edit.html', context={
    'form': form
  })

def destroy(request):
  student = get_object_or_404(Student, id=request.POST['id']).delete()
  
  return redirect('formapp:index')
