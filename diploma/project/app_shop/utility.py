from dataclasses import field
from django.core.cache import cache

from . import tools


class StrMixin:
    def __str__(self):
        return self.title
    
    
class ProductListOrderByMixin:
    paginate_by = 8
    context_object_name = 'products'
    field = ''
    
    def __init__(self,*args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.field_reverse = tools.switch(self.field)
    
    def switch_field(self):
        cache.set(
            tools.format_name_class('field', self),
            cache.get(tools.format_name_class('field_reverse', self))
            )
        cache.set(
            tools.format_name_class('field_reverse', self),
            tools.switch(cache.get(tools.format_name_class('field', self)))
            )
    
    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related('tag')
        field = cache.get_or_set(tools.format_name_class('field', self), self.field)
        field_reverse = cache.get_or_set(tools.format_name_class('field_reverse', self), self.field_reverse)
        
        if field:
            queryset = queryset.order_by(field if self.request.GET.get('page') is None else field_reverse)
            self.switch_field() if self.request.GET.get('page') is None else None

        return queryset