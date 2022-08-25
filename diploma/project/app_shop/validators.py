from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


validate_card_length = RegexValidator(regex=r'\d{4} \d{4}')

def validate_card_even(card_number):
    if int(card_number[-1]) % 2 != 0:
        raise ValidationError('Input even number.')