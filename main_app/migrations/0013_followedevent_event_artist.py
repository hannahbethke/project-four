# Generated by Django 4.1.2 on 2022-10-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_followedevent_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='followedevent',
            name='event_artist',
            field=models.ManyToManyField(to='main_app.artists'),
        ),
    ]
