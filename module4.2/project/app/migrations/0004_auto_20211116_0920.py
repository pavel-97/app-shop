# Generated by Django 2.2 on 2021-11-16 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211116_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='type_of',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.AdvertisementType'),
        ),
    ]
