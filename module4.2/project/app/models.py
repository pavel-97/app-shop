from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, db_index=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.IntegerField(verbose_name='Цена', default=0)
    views_count = models.IntegerField(verbose_name='Кол-во просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements')
    type_of = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                                related_name='advertisements')

    class Meta:
        ordering = ['created_at', ]

class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)
