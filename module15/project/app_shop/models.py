from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Product(models.Model):
    """
    class Product
    """
    name = models.CharField(max_length=100, verbose_name=_('name'))
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=_('price'))

    def str(self):
        return self.name
