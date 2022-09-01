from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _


def max_min_value(value):
    if not (0 <= value <= 100):
        raise ValidationError(_('field must be in range 0 to 100'))
