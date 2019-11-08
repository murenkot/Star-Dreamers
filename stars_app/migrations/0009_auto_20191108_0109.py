# Generated by Django 2.2.7 on 2019-11-08 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stars_app', '0008_auto_20191108_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likephoto',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photolikes_user', to=settings.AUTH_USER_MODEL),
        ),
    ]