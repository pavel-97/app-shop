# Generated by Django 4.0.6 on 2022-07-20 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0023_remove_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(related_name='images', to='app_shop.productimage', verbose_name='image(s)'),
        ),
    ]