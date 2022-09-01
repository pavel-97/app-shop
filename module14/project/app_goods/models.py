from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')
    weight = models.FloatField(verbose_name='вес')


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название категории')

    def __str__(self):
        return self.name