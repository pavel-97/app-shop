# Generated by Django 4.1 on 2022-08-12 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0038_order_total_proce'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_proce',
            new_name='total_price',
        ),
    ]
