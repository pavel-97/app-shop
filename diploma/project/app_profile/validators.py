from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from typing import BinaryIO


phone_number_validator = RegexValidator(regex=r'\+\d{11}')


def validate_image(image_object: BinaryIO) -> None:
    """
    Функция валидатор. Проверяет размер изображения.
    :type image_object: BinaryIO
    :rtype : None
    """
    megabite_limit = 2
    if image_object.file.size > megabite_limit * 1024 *1024:
        raise ValidationError('{} > {}MB'.format(image_object.file, megabite_limit))