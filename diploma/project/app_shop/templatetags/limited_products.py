from django import template


register = template.Library()


@register.filter(name='limited_products')
def limited_products(values):
    return values.filter(productstorage__count__lte=25)[:16]