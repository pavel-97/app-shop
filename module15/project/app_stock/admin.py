from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Stock)
class AdminStock(admin.ModelAdmin):
    list_display = ['title', 'date_start', 'date_end', 'discount']
