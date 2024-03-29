from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    picture = models.FileField(null=True, upload_to='accounts/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email
    

class UserActivateTokenManager(models.Manager):

    def activate_user_by_token(self, token):
        today = timezone.now().date()
        token =get_object_or_404(self, token=token, expired_at__gte=today)
        user = token.user
        user.is_active = True
        user.save()
        

class UserActivateToken(models.Model):
    token = models.UUIDField(db_index=True)
    expired_at = models.DateTimeField()
    user = models.ForeignKey(
        'User',
        on_delete = models.CASCADE
    )

    objects = UserActivateTokenManager()

    class Meta:
        db_table = 'user_activate_tokens'


@receiver(post_save, sender=User)
def publish_token(sender, instance, **kwargs):
    user_activate_token = UserActivateToken.objects.create(
        user = instance,
        token = str(uuid4()),
        expired_at = datetime.now() + timedelta(days=1)
    )
    print(f'http://127.0.0.1:8000/accounts/user_activate/{user_activate_token.token}')