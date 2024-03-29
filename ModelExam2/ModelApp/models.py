from django.db import models

# Create your models here.

class Test(models.Model):
  name = models.CharField(max_length=50)

  class Meta:
    db_table = "tests"

class Test_results(models.Model):
    # id(PK) student_id(FK, int) test_id(FK, int) score(int)
    student = models.ForeignKey(
        "Student",
        on_delete=models.CASCADE,
    )
    test = models.ForeignKey(
       "Test",
       on_delete=models.CASCADE
    )
    score = models.IntegerField()

    class Meta:
       db_table = "test_results"

class Student(models.Model):
    # id(PK) class_id(FK, int) name(VARCHAR(50)) grade(int)
    student_class = models.ForeignKey(
      "Class",
      on_delete=models.CASCADE 
    )
    name = models.CharField(max_length=50)
    grade = models.IntegerField()

    class Meta:
      db_table = "students"

class Class(models.Model):
    # id(PK) name(VARCHAR(50))
    name = models.CharField(max_length=50)

    class Meta:
      db_table = "classes"

