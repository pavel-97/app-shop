# Generated by Django 4.1 on 2022-08-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0040_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, verbose_name='comment'),
        ),
    ]