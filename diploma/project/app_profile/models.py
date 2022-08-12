from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from . import validators
from . import tools

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name=_('balance'))
    avatar = models.ImageField(upload_to=tools.get_path ,blank=True, null=True)
    telephon_number = models.CharField(max_length=12, unique=True, blank=True, validators=(validators.phone_number_validator, ), verbose_name=_('telephon number'))
    city = models.CharField(max_length=100, blank=True, verbose_name=_('city'))
    address = models.CharField(max_length=150, blank=True, verbose_name=_('address'))
    
    def __str__(self):
        return self.user.username