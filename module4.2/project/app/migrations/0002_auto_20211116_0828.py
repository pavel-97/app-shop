# Generated by Django 2.2 on 2021-11-16 08:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='Кол-во просмотров'),
        ),
    ]