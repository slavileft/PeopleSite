# Generated by Django 4.1.3 on 2022-12-09 11:41

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dduser',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, default=1, max_length=255),
            preserve_default=False,
        ),
    ]
