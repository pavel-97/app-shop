from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AdvertisementType)
class AdvertisementTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AdvertisementAuthor)
class AdvertisementAuthorAdmin(admin.ModelAdmin):
    pass
