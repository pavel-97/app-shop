# Generated by Django 2.2 on 2022-06-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0008_product_other_characteristic'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='additional_info',
            field=models.TextField(blank=True, verbose_name='additional info'),
        ),
    ]
