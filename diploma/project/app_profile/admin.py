from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db.models import Count

from . import models

# Register your models here.


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_photo')
    
    def get_photo(self, obj):
        if obj.avatar:
            return mark_safe('<img src="{}" width=75>'.format(obj.avatar.url))
        return '-'
    
    get_photo.short_description = 'avatar'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')


@admin.register(models.HistoryOrder)
class HistoryOrderAdmin(admin.ModelAdmin):
    list_display = ('profile', 'orders_count')
    
    def orders_count(self, obj):
        return obj.orders__count
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('profile__user').prefetch_related('orders').annotate(Count('orders'))