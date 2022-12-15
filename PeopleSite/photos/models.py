from cloudinary import models as cloudinary_models
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Photo(models.Model):
    MAX_DESCRIPTION_LENGTH = 300

    photo = cloudinary_models.CloudinaryField(
        null=False,
        blank=True,
    )
    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
    )
    publication_date = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=True,
    )

    person = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.description
