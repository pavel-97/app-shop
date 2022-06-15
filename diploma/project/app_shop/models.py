from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from . import utility
from . import tools

# Create your models here.


class Category(utility.StrMixin, models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name=_('title'))


class Product(utility.StrMixin, models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name=_('title'))
    slug = models.SlugField(max_length=150,verbose_name=_('slug'), blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_('category'))
    tag = models.ManyToManyField('Tag', verbose_name=_('tag(s)'))
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('price'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    characteristic = models.TextField(blank=True ,verbose_name=_('characteristic'))
    other_characteristic = models.TextField(blank=True ,verbose_name=_('other characteristic'))
    additional_info = models.TextField(blank=True, verbose_name=_('additional info'))

    def save(self, *args, **kwargs):
        self.slug = tools.make_slug(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('product', kwargs={'slug': self.slug})


class Tag(utility.StrMixin, models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name=_('title'))