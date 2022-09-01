from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from . import contants

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    record = models.ManyToManyField('Record')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title


class Record(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    author = models.ManyToManyField('Author')
    moderator = models.ForeignKey('Moderator', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=contants.TITLE_CHOICE, null=True)

    def __str__(self):
        return self.user.username


class Moderator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))

    def __str__(self):
        return self.user.username
