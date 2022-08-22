from django import template


register = template.Library()


@register.filter(name='total_price')
def total_price(values):
    total_price = 0
    try:
        for value, count in values.items():
            total_price += value.price * int(count)
    except AttributeError:
        pass
    return total_price