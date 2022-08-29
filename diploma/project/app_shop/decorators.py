from types import FunctionType

from django.core.cache import cache
from django.db.models import F
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy

from . import models


def except_value_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except ValueError:
            result = ''
        return result
    return wrapper


def except_validation_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except ValidationError:
            return redirect('basket')
        return result
    return wrapper


def except_error_with_arg(_func=None, *, return_object=dict(), **_kwargs):
    def except_attr_error(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except (AttributeError, TypeError):
                result = return_object if not isinstance(return_object, FunctionType) else return_object(**_kwargs)
            return result
        return wrapper
    if _func is None:
        return except_attr_error
    return except_attr_error(_func)


def add_view(func):
    def wrapper(*args, **kwargs):
        model = args[0].model
        instance = model.objects.filter(slug=kwargs.get('slug'))
        instance.update(views=F('views') + 1)
        result = func(*args, **kwargs)
        return result
    return wrapper


def delete_basket(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        cache.delete('basket')
        return result
    return wrapper


def add_review(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        product = args[0].get_context_data().get('product')
        review = cache.get('review', list())
        if not product in review:
            review.append(product)
        cache.set('review', review)
        return result
    return wrapper

def permission_denied(func):
    def wrapper(*args, **kwargs):
        request = args[1]
        if request.user.pk:
            result = func(*args, **kwargs)
        else:
            result = redirect(reverse_lazy('login'))
        return result
    return wrapper


def include_delivery(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if all([product_order.product.free_delivery for product_order in result.product_order.all()]):
            delivery = {'ORDINARY': models.OrderPriceForDelivery.objects.get(title='ordinary price'), 
                        'EXPRESS': models.OrderPriceForDelivery.objects.get(title='express price')}
        else:    
            delivery = {'ORDINARY': models.OrderPriceForDelivery.objects.get(title='ordinary price') if result.total_price < 2000 else 0, 
                        'EXPRESS': models.OrderPriceForDelivery.objects.get(title='ordinary price')}
        result.total_price = F('total_price') + delivery.get(result.delivery)
        return result
    return wrapper