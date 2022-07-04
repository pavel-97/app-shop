from transliterate import translit, detect_language
from django.core.cache import cache

from . import decorators


def switch(string):
    if string.startswith('-'):
        string = string.replace('-', '')
    else:
        string = '-' + string
    return string


def make_slug(title):
    language = detect_language(title)
    slug = title

    if language == 'ru':
        slug = translit(title, 'en')

    return '-'.join(slug.lower().replace('\'', '').replace('\"', '').split())


@decorators.except_value_error
def get_dict_characteristics(other_characteristics):
    result = dict()
    for line in other_characteristics.split('\n'):
        key, value = line.split(':')
        result[key] = value
    return result


def format_name_class(name, obj):
    return '{}_{}'.format(name, obj.__class__)


def set_filter(instance, filter_name, init_value=None):
    
    if instance.request.GET:
        filters = init_value

        if not filters:
            filters = cache.get(filter_name)
            if filters is None: filters = init_value

        else:
            cache.set(filter_name, filters)
        
    else:
        cache.delete(filter_name)
        filters = init_value
        
    return filters
        