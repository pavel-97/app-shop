from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Blog)
class AdminBlog(admin.ModelAdmin):
    pass


@admin.register(models.Record)
class AdminRecord(admin.ModelAdmin):
    pass


@admin.register(models.Author)
class AdminAuthor(admin.ModelAdmin):
    pass


@admin.register(models.Moderator)
class AdminModerator(admin.ModelAdmin):
    pass
