# Generated by Django 5.0.4 on 2024-05-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataBase', '0002_alter_music_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/file/music/thumbnails'),
        ),
    ]
