# Generated by Django 4.2.7 on 2023-11-23 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapphotos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapphoto',
            name='image',
            field=models.URLField(),
        ),
    ]
