from django import template


register = template.Library()


@register.filter(name='favorite_categories')
def favorite_categories(values):
    return values.order_by('-product__views__max')[:3]