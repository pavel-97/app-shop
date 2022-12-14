import profile
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from . import validators
from . import tools

from app_shop.validators import validate_card_even, validate_card_length

# Create your models here.


class Profile(models.Model):
    """
    Класс Profile. Наследние класса Model.
    Реализует таблицу с профилями пользователей.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name=_('balance'))
    avatar = models.ImageField(upload_to=tools.get_path ,blank=True, null=True, validators=[validators.validate_image, ], verbose_name=_('avatar'))
    telephon_number = models.CharField(max_length=12, unique=True, blank=True, validators=(validators.phone_number_validator, ), verbose_name=_('telephon number'))
    city = models.CharField(max_length=100, blank=True, verbose_name=_('city'))
    address = models.CharField(max_length=150, blank=True, verbose_name=_('address'))
    card = models.CharField(max_length=8, blank=True, validators=[validate_card_even, validate_card_length], verbose_name=_('card'))
    
    def __str__(self):
        return self.user.username
    
    
class HistoryOrder(models.Model):
    """
    Класс HistoryOrder. Наследние класса Model.
    Реализует таблицу с историями пользователей.
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name=_('profile'))
    orders = models.ManyToManyField('app_shop.Order', verbose_name=_('orders'))
    
    def __str__(self):
        return 'history: {}'.format(self.profile.user.username)