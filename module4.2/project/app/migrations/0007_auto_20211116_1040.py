# Generated by Django 2.2 on 2021-11-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20211116_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(db_index=True, max_length=1500),
        ),
    ]
