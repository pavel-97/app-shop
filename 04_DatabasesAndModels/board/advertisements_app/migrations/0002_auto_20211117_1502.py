# Generated by Django 2.2 on 2021-11-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisementauthor',
            name='telephone_number',
            field=models.CharField(max_length=10),
        ),
    ]
