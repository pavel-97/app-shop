# Generated by Django 4.0.6 on 2022-07-17 11:46

import app_profile.tools
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0003_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to=app_profile.tools.get_path),
        ),
    ]