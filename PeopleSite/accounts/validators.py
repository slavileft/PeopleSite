from django.core.exceptions import ValidationError

def is_alphabetical(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Only letters are allowed')