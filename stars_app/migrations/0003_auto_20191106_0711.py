# Generated by Django 2.2.7 on 2019-11-06 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars_app', '0002_photo_hdurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
