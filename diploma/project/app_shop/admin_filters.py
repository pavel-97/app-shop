from django.contrib import admin

from . import models


class FilterOrder(admin.SimpleListFilter):
    title = 'orders'
    parameter_name = 'order'
    
    def lookups(self, request, model_admin):
        orders = models.Order.objects.select_related('profile__user')
        list_order = []
        for order in orders:
            list_order.append(
                (order.pk, order)
            )
        return list_order
    
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(order=self.value())
        return queryset