# Generated by Django 2.2.7 on 2019-11-08 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stars_app', '0007_auto_20191107_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photolikes_photo', to='stars_app.Photo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photolikes_user', to='stars_app.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postlikes_post', to='stars_app.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postlikes_user', to='stars_app.Photo')),
            ],
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]