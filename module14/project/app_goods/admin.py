from django.contrib import admin

from . import models
# Register your models here.


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass