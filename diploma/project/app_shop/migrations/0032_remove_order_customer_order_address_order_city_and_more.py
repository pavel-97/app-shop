# Generated by Django 4.0.6 on 2022-07-26 14:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0011_profile_address'),
        ('app_shop', '0031_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=150, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=100, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_profile.profile', verbose_name='profile'),
        ),
        migrations.AddField(
            model_name='order',
            name='telephon_number',
            field=models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(regex='\\+\\d{11}')], verbose_name='telephon_number'),
        ),
    ]
