from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            password=password,
            username=username
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    website = models.URLField(null=True)
    picture = models.FileField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    score = models.IntegerField()
    school = models.ForeignKey(
        'School',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'students'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name + " : " + str(self.age)
    
class School(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'schools'
        verbose_name_plural = 'Schools'

    def __str__(self):
        return self.name