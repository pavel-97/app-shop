# Generated by Django 2.2 on 2021-11-16 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20211116_1043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['created_at']},
        ),
    ]
