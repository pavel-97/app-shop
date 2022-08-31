from datetime import date
from typing import Any


def get_path(instance: Any, filename: str) -> str:
    """
    Функция возвращает путь к файлу.
    :type insance: Any
    :type filename: str
    :rtype: str
    """
    format_img = filename.split('.')[-1]
    loaded_at = date.today().strftime('%d-%m-%Y')
    return 'app_profile/{}/{}.{}'.format(
        instance.user.username,
        loaded_at,
        format_img)