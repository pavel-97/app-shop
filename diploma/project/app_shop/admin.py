from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CategoryMPTT)
class CategoryMPTTAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'price')


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductStorage)
class ProductStorageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    pass