from django import template


register = template.Library()


@register.filter(name='total_price')
def total_price(values):
    print('-->',values)
    total_price = 0
    for value, count in values.items():
        total_price += value.price * int(count)
    return total_price