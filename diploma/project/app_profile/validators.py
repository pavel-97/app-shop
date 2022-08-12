from django.core.validators import RegexValidator


phone_number_validator = RegexValidator(regex=r'\+\d{11}')