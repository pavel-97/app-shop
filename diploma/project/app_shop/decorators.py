from django.core.cache import cache
from django.db.models import F
from django.core.exceptions import ValidationError
from django.shortcuts import redirect


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


def except_attr_error_with_arg(_func=None, *, return_object=dict()):
    def except_attr_error(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except AttributeError:
                result = return_object
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
