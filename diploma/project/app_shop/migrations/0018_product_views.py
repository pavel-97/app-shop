# Generated by Django 4.0.6 on 2022-07-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0017_remove_productimage_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='views'),
        ),
    ]
