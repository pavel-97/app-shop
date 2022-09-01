from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.News)
class AdminNews(admin.ModelAdmin):
    pass
