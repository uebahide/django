from django.db import models
from accounts.models import User

# Create your models here.

class ThemeManager(models.Manager):
    def fetch_all(self):
       return self.order_by('id').all()

class Theme(models.Model):
    title = models.CharField(max_length=120)
    user = models.ForeignKey(
        'accounts.User',
        on_delete = models.CASCADE
    )

    objects = ThemeManager()

    class Meta:
      db_table = 'themes'


class CommentManager(models.Manager):
   def fetch_all_by_theme(self, theme):
      return self.filter(theme=theme).order_by('id').all()

class Comment(models.Model):
    content = models.CharField(max_length=255)
    theme = models.ForeignKey(
       'Theme',
       on_delete = models.CASCADE
    )
    user = models.ForeignKey(
       'accounts.User',
       on_delete = models.CASCADE
    )

    objects = CommentManager()

    class Meta:
       db_table = 'comments'
