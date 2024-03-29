from django.db import models

# Create your models here.

class Student(models.Model):
  # class_id(FK, int) name(VARCHAR(50)) grade(int) picture(file)
  student_class = models.ForeignKey(
    'Class',
    on_delete=models.CASCADE
  )
  name = models.CharField(max_length=50)
  grade = models.IntegerField()
  picture = models.FileField(upload_to='documents/')

  class Meta:
    db_table="students"

class Class(models.Model):
  name = models.CharField(max_length=50)

  class Meta:
    db_table="classes"