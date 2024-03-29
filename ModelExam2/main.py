import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam2.settings')
from django import setup
setup()

from ModelApp.models import Student, Class, Test, Test_results

import random

Class.objects.bulk_create(
  [
    Class(name='ClassA'),
    Class(name='ClassB'),
    Class(name='ClassC'),
    Class(name='ClassD'),
    Class(name='ClassE'),
    Class(name='ClassF'),
    Class(name='ClassG'),
    Class(name='ClassH'),
    Class(name='ClassI'),
    Class(name='ClassJ')
  ]
)

Student.objects.bulk_create(
  [
    Student(student_class_id=1, name='studentB', grade=1),
    Student(student_class_id=2, name='studentC', grade=1),
    Student(student_class_id=3, name='studentD', grade=1),
    Student(student_class_id=4, name='studentE', grade=1),
    Student(student_class_id=5, name='studentF', grade=1),
    Student(student_class_id=6, name='studentG', grade=1),
    Student(student_class_id=7, name='studentH', grade=1),
    Student(student_class_id=8, name='studentI', grade=1),
    Student(student_class_id=9, name='studentJ', grade=1),
    Student(student_class_id=10, name='studentK', grade=1),
  ]
)

Test.objects.bulk_create(
  [
    Test(name="Math"),
    Test(name="English"),
    Test(name="Language"),
  ]
)

Test_results.objects.bulk_create(
  [
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
  ]
)
