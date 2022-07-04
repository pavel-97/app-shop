

def except_value_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except ValueError:
            result = ''
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