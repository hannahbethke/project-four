# Generated by Django 4.1.2 on 2022-10-08 18:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_artists_artist_seatgeek_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artists',
            name='fav_artists',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
