# Generated by Django 4.0.6 on 2022-08-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0036_categorymptt_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='free_delivery',
            field=models.BooleanField(default=False, verbose_name='free delivery'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_exist',
            field=models.BooleanField(default=True, verbose_name='is exist'),
        ),
    ]
