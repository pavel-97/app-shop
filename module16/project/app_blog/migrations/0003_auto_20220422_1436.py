# Generated by Django 2.2 on 2022-04-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_auto_20220422_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='status',
            field=models.CharField(choices=[('BEGINNER', 'beginner'), ('ADVANCED', 'advanced'), ('EXPERT', 'expert')], max_length=3, null=True),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
