import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FormExam.settings')
from django import setup
setup()

from FormApp.models import Class

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
