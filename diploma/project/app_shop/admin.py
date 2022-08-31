from django.contrib import admin
from django.utils.safestring import mark_safe

from mptt.admin import DraggableMPTTAdmin

from . import models
from . import admin_filters

# Register your models here.


@admin.register(models.CategoryMPTT)
class CategoryMPTTAdmin(DraggableMPTTAdmin):
    """
    Класс CategoryMPTTAdmin. Наследник класса DraggableMPTTAdmin.
    Отображает ссылку на таблицу модели CategoryMPTT в административной панели.
    """
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Класс ProductAdmin. Наследник класса ModelAdmin.
    Отображает ссылку на таблицу модели Product в административной панели.
    """
    list_display = ('title', 'get_content_image', 'price', 'updated_at')
    search_fields = ('title', 'category', )
    list_filter = ('is_exist', 'free_delivery', )
    readonly_fields = ('views', )
    
    def get_content_image(self, obj):
        images = obj.images.all()
        if images:
            return mark_safe('<img src="{}" width=75>'.format(images.filter(content_image=True).first().image.url))
        return '-'
    
    get_content_image.short_description = 'photo'
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('images')


@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    """
    Класс ProductImageAdmin. Наследник класса ModelAdmin.
    Отображает ссылку на таблицу модели ProductImage в административной панели.
    """
    list_display = ('product', 'get_photo')
    
    def get_photo(self, obj):
        return mark_safe('<img src="{}" width=95 height=75>'.format(obj.image.url))
    
    get_photo.short_description = 'photo'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('product')


@admin.register(models.ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    """
    Класс ProductCommentAdmin. Наследник класса ModelAdmin.
    Отображает ссылку на таблицу модели ProductComment в административной панели.
    """
    list_display = ('profile', 'product', 'created_at')
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('profile__user', 'product')


@admin.register(models.ProductStorage)
class ProductStorageAdmin(admin.ModelAdmin):
    list_display = ('product', 'count')
    search_fields = ('product__title', )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('product')


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('profile', 'city', 'total_price', 'pay', 'delivery')
    search_fields = ('profile__user__username', 'city', 'telephon_number')
    list_filter = ('pay', 'delivery', )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('profile__user').prefetch_related('product_order')


@admin.register(models.ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    """
    Класс ProductOrderAdmin. Наследник класса ModelAdmin.
    Отображает ссылку на таблицу модели ProductOrder в административной панели.
    """
    list_display = ('product', 'count', 'get_order', )
    list_filter = (admin_filters.FilterOrder, )
    
    def get_order(self, obj):
        return '{}'.format(''.join([str(order.pk) for order in obj.order_set.all()]))
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('order_set')
    
    
@admin.register(models.OrderPriceForDelivery)
class OrderPriceForDeliveryAdmin(admin.ModelAdmin):
    pass