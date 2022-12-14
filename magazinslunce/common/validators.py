from django.core import exceptions
from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed')


def validate_only_numbers(value):
    for ch in value:
        if not ch.isdigit():
            raise exceptions.ValidationError('Only numbers are allowed')


def validate_file_size(value):
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MB.')

