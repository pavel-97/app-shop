# Generated by Django 4.0.6 on 2022-07-20 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0022_remove_product_comments_productcomment_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
    ]
