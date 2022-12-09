from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def is_alphabetical(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Only letters are allowed')


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_value(cls):
        return max(len(name) for name, value in cls.choices())


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    do_not_show = 'Do not show'


class EyesColor(ChoicesEnumMixin, Enum):
    black = 'Black'
    brown = 'Brown'
    blue = 'Blue'
    green = 'Green'
    hazel = 'Hazel'
    amber = 'Amber'
    grey = 'Grey'


class DdUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            is_alphabetical,
        ),
        null=True,
        blank=False,
    )
    last_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            is_alphabetical,
        ),
        null=True,
        blank=False,
    )
    age = models.PositiveIntegerField(
        validators=(
            MinValueValidator(18),
        ),
        null=True,
        blank=False,
    )
    height = models.FloatField(
        validators=(
            MinValueValidator(0),
        ),
        null=True,
        blank=True,
    )
    weight = models.FloatField(
        validators=(
            MinValueValidator(0),
        ),
        null=True,
        blank=True,
    )
    eyes_color = models.CharField(
        max_length=EyesColor.max_value(),
        choices=EyesColor.choices(),
        null=True,
        blank=True,
    )
    # TODO make enum for hair_color
    hair_color = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    # TODO change to cloudinary picture
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=Gender.max_value(),
        choices=Gender.choices(),
        null=True,
        blank=False,
    )

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)