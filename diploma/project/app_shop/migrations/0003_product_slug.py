# Generated by Django 2.2 on 2022-06-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0002_auto_20220611_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='slug'),
        ),
    ]
