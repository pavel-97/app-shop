from django.core.cache import cache

from . import tools
from . import decorators


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
            queryset = queryset.order_by(field if all(
                self.request.GET.get(_) is None for _ in ('page', 'price', 'title', 'query') 
                ) else field_reverse)
            self.switch_field() if all(
                self.request.GET.get(_) is None for _ in ('page', 'price', 'title', 'query')
                ) else None

        return queryset
    
    
class ProductQuerysetFilterMixin:
    
    @decorators.except_attr_error_with_arg(return_object=dict())
    def get_filters(self):
        price_range, title_filter = [self.request.GET.get(_) for _ in ('price', 'title')]
        price_min, price_max = [int(_) for _ in price_range.split(';')]
        return {
            'title__icontains': title_filter,
            'price__lte': price_max,
            'price__gte': price_min,
        }
    
    def get_queryset(self):
        
        filters = tools.set_filter(
            self,
            'filters',
            self.get_filters()
            )

        return super().get_queryset().filter(**filters)
    
    
class SearchMixin:
    def get_queryset(self):
        query = tools.set_filter(
            self,
            'query',
            self.request.GET.get('query', '')
            )

        return super().get_queryset().filter(title__contains=query)