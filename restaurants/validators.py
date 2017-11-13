from django.core.exceptions import ValidationError
import string

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            ('%(value)s is not an even number'),
            params={'value':value},
        )

def clean_email(value):

    if ".edu" in value:
        raise ValidationError("We do not accept edu emails")

CATEGORIES = [
    'PIZZA',
    'FAST FOOD',
    'ORIENTAL',
    'ITALIAN',
    'HAMBURGUER'
]

def validate_category(value):

    if not str.upper(value) in CATEGORIES:
        raise ValidationError("The Category should be: {s}". format(s=CATEGORIES))
