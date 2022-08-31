from transliterate import translit, detect_language
from django.core.cache import cache
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.models import Model
from django.views.generic import ListView

from typing import Dict, Any, Optional, Type

from . import decorators
from . import models


def switch(string: str) -> str:
    """
    Функция принимает строку. Меняет ее значение и возращает строку.
    :type string: type
    :rtype: str
    """
    if string.startswith('-'):
        string = string.replace('-', '')
    else:
        string = '-' + string
    return string


def make_slug(title: str) -> str:
    """
    Функция принимает строку. Меняет ее значение и возращает строку.
    :type string: str
    :rtype: str
    """
    language = detect_language(title)
    slug = title

    if language == 'ru':
        slug = translit(title, 'en')

    return '-'.join(slug.lower().replace('\'', '').replace('\"', '').split())


@decorators.except_value_error
def get_dict_characteristics(other_characteristics: str) -> Dict:
    """
    Функция принимает строку. Обрабатывает ее значение и возращает словарю.
    :type other_characteristics: str
    :rtype: Dict
    """
    result = dict()
    for line in other_characteristics.split('\n'):
        key, value = line.split(':')
        result[key] = value
    return result


def format_name_class(name: str, obj: Any) -> str:
    """
    Функция принимает строку и экземпляр класса. Обрабатывает из значения и возращает строку.
    :type name: str
    :type obj: Any
    :rtype: str
    """
    return '{}_{}'.format(name, obj.__class__)


def set_filter(instance: Type[ListView], filter_name: str, init_value:Optional[Dict]=None) -> Dict:
    """
    Функция принимает объект представления, название фильтра и первоначально значение.
    Обрабатывает значения, записывает/дастает их из кэша и возврашает словарь.
    :instance
    :type filter_name: str
    :type init_value: Dict или None
    :rtype: Dict
    """
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
        
        
def get_path(instance: Type[Model], filename: str) -> str:
    """
    Функция принимает объект модели и файл. Возвращает путь к файлу.
    """
    format_img = filename.split('.')[-1]
    return 'app_shop/{}/{}.{}'.format(
        instance.product.title,
        instance.title,
        format_img
    )


def get_path_category(instance: Type[Model], filename: str) -> str:
    """
    Функция принимает объект модели и файл. Возвращает путь к файлу.
    """
    format_img = filename.split('.')[-1]
    return 'app_shop/{}/{}.{}'.format(
        'categories',
        instance.title,
        format_img
    )

    
def add_product_to_basket(product:Type['app_shop.models.Product'], count: int=1) -> None:
    """
    Функция добавляет товар в корзину.
    """
    basket = cache.get('basket', dict())
    if product not in basket:
        basket[product]=count
        cache.set('basket', basket)
    return None


def add_count_product_to_basket(dict_GET: Dict) -> None:
    """
    Функция добавляет количество продуктов уже присутствующих в корзине.
    """
    basket = cache.get('basket')
    product_dict = {product.title: product for product in basket}
    for key in dict_GET:
        product_title = key.split('_')[0]
        product = product_dict.get(product_title)
        basket[product] = dict_GET.get(key)
    cache.set('basket', basket)
    return None
        

def delete_product_from_basket(product: Type['app_shop.models.Product']) -> None:
    """"
    Функция удаляет товар из корзины.
    """
    basket = cache.get('basket', dict())
    if product in basket:
        basket.pop(product)
        cache.set('basket', basket)
    return None


def get_or_error(model: Type[Model], product: Type['app_shop.models.Product']) -> Model:
    """
    Функция получает объет из таблицы БД. Если такого нет, то вызывает исключение ObjectDoesNotExist.
    """
    try:
        obj = model.objects.get(product=product)
    except ObjectDoesNotExist:
        raise ValidationError('{} is absent in shop'.format(product.title))
    return obj