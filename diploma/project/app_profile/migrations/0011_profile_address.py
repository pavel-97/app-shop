# Generated by Django 4.0.6 on 2022-07-26 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0010_profile_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=150, verbose_name='address'),
        ),
    ]
