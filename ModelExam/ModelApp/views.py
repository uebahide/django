from django.shortcuts import render
from ModelApp.models import *

# Create your views here.

def home(request, sid):
  student = Students.objects.filter(id=sid).first()

  # 7. クラス毎の、各科目のテストの合計、平均、最大、最小を表示する。
  
  math_total = 0
  eng_total = 0
  lung_total = 0

  

  return render(request, 'home.html', context = {
    'student' : student,
    'classes' : classes
  })