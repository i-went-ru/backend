# Generated by Django 4.2.7 on 2023-11-22 01:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_rename_datetime_tour_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='comment',
            field=models.CharField(default=datetime.datetime(2023, 11, 22, 1, 18, 49, 342491, tzinfo=datetime.timezone.utc), max_length=2500),
            preserve_default=False,
        ),
    ]
