from django import template


register = template.Library()


@register.filter(name='top_products')
def top_products(values):
    return values.order_by('-views')[:8]