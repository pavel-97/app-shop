from django.contrib import admin

from . import models
# Register your models here.


@admin.register(models.Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'id', 'price']
