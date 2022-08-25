# Generated by Django 4.0.6 on 2022-07-16 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0003_profile_avatar'),
        ('app_shop', '0019_productimage_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shop.product', verbose_name='product')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_profile.profile', verbose_name='profile')),
            ],
        ),
    ]