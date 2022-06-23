from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))
    balance = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('balance'))
    
    def __str__(self):
        return self.user.username