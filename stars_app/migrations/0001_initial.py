# Generated by Django 2.2.7 on 2019-11-06 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=10)),
                ('explanation', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
    ]
