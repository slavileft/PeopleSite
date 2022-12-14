# Generated by Django 4.1.3 on 2022-12-09 11:57

import PeopleSite.accounts.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_dduser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dduser',
            name='last_name',
            field=models.CharField(max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), PeopleSite.accounts.validators.is_alphabetical]),
        ),
    ]
