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
        
        
def get_path(instance, filename):
    format_img = filename.split('.')[-1]
    return 'app_shop/{}/{}.{}'.format(
        instance.product.title,
        instance.title,
        format_img
    )
    
    
def add_product_to_basket(product, count=1):
    basket = cache.get('basket', dict())
    if product not in basket:
        basket[product]=count
        cache.set('basket', basket)
    return None


def add_count_product_to_basket(dict_GET):
    basket = cache.get('basket')
    product_dict = {product.title: product for product in basket}
    for key in dict_GET:
        product_title = key.split('_')[0]
        product = product_dict.get(product_title)
        basket[product] = dict_GET.get(key)
    cache.set('basket', basket)
    return None
        

def delete_product_from_basket(product):
    basket = cache.get('basket', dict())
    if product in basket:
        basket.pop(product)
        cache.set('basket', basket)
    return None