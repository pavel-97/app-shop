# Generated by Django 4.1 on 2022-08-26 08:50

import app_shop.tools
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0048_alter_categorymptt_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymptt',
            name='image',
            field=models.FileField(blank=True, default='media/app_shop/categories/Electronics.svg', null=True, upload_to=app_shop.tools.get_path_category, verbose_name='image'),
        ),
    ]