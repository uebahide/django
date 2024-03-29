import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Students, Classes, Test_results, Tests

import random

Classes.objects.bulk_create([
  Classes(name='classA'),
  Classes(name='classB'),
  Classes(name='classC'),
  Classes(name='classD'),
  Classes(name='classE'),
  Classes(name='classF'),
  Classes(name='classG'),
  Classes(name='classH'),
  Classes(name='classI'),
  Classes(name='classJ'),
])

Students.objects.bulk_create([
  Students(_class_id=1, name='studentA', grade=1),
  Students(_class_id=2, name='studentB', grade=1),
  Students(_class_id=3, name='studentC', grade=1),
  Students(_class_id=4, name='studentD', grade=1),
  Students(_class_id=5, name='studentE', grade=1),
  Students(_class_id=6, name='studentF', grade=1),
  Students(_class_id=7, name='studentG', grade=1),
  Students(_class_id=8, name='studentH', grade=1),
  Students(_class_id=9, name='studentI', grade=1),
  Students(_class_id=10, name='studentJ', grade=1),
])

Tests.objects.bulk_create([
  Tests(name='Math'),
  Tests(name='English'),
  Tests(name='Language'),
])

Test_results.objects.bulk_create([
  Test_results(student_id=1, test_id=1, score=random.randint(50, 100)),
  Test_results(student_id=1, test_id=2, score=random.randint(50, 100)),
  Test_results(student_id=1, test_id=3, score=random.randint(50, 100)),

  Test_results(student_id=2, test_id=1, score=random.randint(50, 100)),
  Test_results(student_id=2, test_id=2, score=random.randint(50, 100)),
  Test_results(student_id=2, test_id=3, score=random.randint(50, 100)),

  Test_results(student_id=3, test_id=1, score=random.randint(50, 100)),
  Test_results(student_id=3, test_id=2, score=random.randint(50, 100)),
  Test_results(student_id=3, test_id=3, score=random.randint(50, 100)),

  Test_results(student_id=4, test_id=1, score=random.randint(50, 100)),
  Test_results(student_id=4, test_id=2, score=random.randint(50, 100)),
  Test_results(student_id=4, test_id=3, score=random.randint(50, 100)),

  Test_results(student_id=5, test_id=1, score=random.randint(50, 100)),
  Test_results(student_id=5, test_id=2, score=random.randint(50, 100)),
  Test_results(student_id=5, test_id=3, score=random.randint(50, 100)),

  Test_results(student_id=6, test_id=1, score=random.randint(50, 100)),
  Test_results(student_id=6, test_id=2, score=random.randint(50, 100)),
  Test_results(student_id=6, test_id=3, score=random.randint(50, 100)),

  Test_results(student_id=7, test_id=1, score=random.randint(50, 100)),
  Test_results(student_id=7, test_id=2, score=random.randint(50, 100)),
  Test_results(student_id=7, test_id=3, score=random.randint(50, 100)),

  Test_results(student_id=8, test_id=1, score=random.randint(50, 100)),
  Test_results(student_id=8, test_id=2, score=random.randint(50, 100)),
  Test_results(student_id=8, test_id=3, score=random.randint(50, 100)),

  Test_results(student_id=9, test_id=1, score=random.randint(50, 100)),
  Test_results(student_id=9, test_id=2, score=random.randint(50, 100)),
  Test_results(student_id=9, test_id=3, score=random.randint(50, 100)),

  Test_results(student_id=10, test_id=1, score=random.randint(50, 100)),
  Test_results(student_id=10, test_id=2, score=random.randint(50, 100)),
  Test_results(student_id=10, test_id=3, score=random.randint(50, 100)),
])

# Tests.objects.all().delete()
# Students.objects.all().delete()
# Test_results.objects.all().delete()
# Classes.objects.all().delete()