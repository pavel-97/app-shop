from django.db import models
from django.utils.translation import gettext_lazy as _

from . import validators
# Create your models here.


class Stock(models.Model):
    title = models.CharField(max_length=250, verbose_name=_('title'))
    date_start = models.DateField(auto_now_add=True, verbose_name=_('date start'))
    date_end = models.DateField(verbose_name=_('date end'))
    discount = models.IntegerField(validators=[validators.max_min_value])

    def __str__(self):
        return self.title
