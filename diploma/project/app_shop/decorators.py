

def except_value_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except ValueError:
            result = ''
        return result
    return wrapper