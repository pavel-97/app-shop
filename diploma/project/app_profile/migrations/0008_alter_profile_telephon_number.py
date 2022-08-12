# Generated by Django 4.0.6 on 2022-07-18 20:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0007_alter_profile_telephon_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='telephon_number',
            field=models.CharField(blank=True, max_length=12, unique=True, validators=[django.core.validators.RegexValidator(regex='\\+\\d{11}')], verbose_name='telephone number'),
        ),
    ]
