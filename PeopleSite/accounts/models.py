from cloudinary import models as cloudinary_models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from PeopleSite.accounts.utils import EyesColor, HairColor, Gender
from PeopleSite.accounts.validators import is_alphabetical


class DdUser(AbstractUser):
    MIN_FIRST_NAME_LENGTH = 2
    MAX_FIRST_NAME_LENGTH = 30
    MIN_LAST_NAME_LENGTH = 2
    MAX_LAST_NAME_LENGTH = 30
    MIN_AGE = 18
    MIN_HEIGHT = 0
    MIN_WEIGHT = 0
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_FIRST_NAME_LENGTH, message='The required name must have at least 2 letters.'),
            is_alphabetical,
        ),
        null=True,
        blank=False,
    )
    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_LAST_NAME_LENGTH, message='The required name must have at least 2 letters.'),
            is_alphabetical,
        ),
        null=True,
        blank=False,
    )
    age = models.PositiveIntegerField(
        validators=(
            MinValueValidator(MIN_AGE, message='You must have at least 18 years to register in this site!'),
        ),
        null=True,
        blank=False,
    )
    height = models.FloatField(
        validators=(
            MinValueValidator(MIN_HEIGHT, message='You cannot put negative value for height!'),
        ),
        null=True,
        blank=True,
    )
    weight = models.FloatField(
        validators=(
            MinValueValidator(MIN_WEIGHT, message='You cannot put negative value for weight!'),
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
    hair_color = models.CharField(
        max_length=HairColor.max_value(),
        choices=HairColor.choices(),
        null=True,
        blank=True,
    )
    profile_picture = cloudinary_models.CloudinaryField(
        null=False,
        blank=True,
    )
    gender = models.CharField(
        max_length=Gender.max_value(),
        choices=Gender.choices(),
        null=True,
        blank=False,
    )

    def __str__(self):
        return self.get_full_name()
