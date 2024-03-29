from django.db import models

# Create your models here.

class Tests(models.Model):
  name = models.CharField(max_length=50)

  class Meta:
    db_table = 'tests'

class Classes(models.Model):
  name = models.CharField(max_length=50)

  class Meta:
    db_table = 'classes'

class Students(models.Model):
  _class = models.ForeignKey(
    'classes',
    on_delete = models.CASCADE
  )
  name = models.CharField(max_length=50)
  grade = models.IntegerField()

  class Meta:
    db_table = 'students'

class  Test_results(models.Model):
  student = models.ForeignKey(
    'students',
    on_delete = models.CASCADE
  )
  test = models.ForeignKey(
    'tests',
    on_delete = models.CASCADE
  )
  score = models.IntegerField()

  class Meta:
    db_table = 'test_results'

