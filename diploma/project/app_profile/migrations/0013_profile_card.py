# Generated by Django 4.1 on 2022-08-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0012_historyorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='card',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='card'),
        ),
    ]
