from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'), default='qwerty')
    created_at = models.DateTimeField(auto_now=True, verbose_name=_('created at'))
    publicated_at = models.DateTimeField(auto_now_add=True, verbose_name=_('publicated at'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('detail_news', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = _('News')
