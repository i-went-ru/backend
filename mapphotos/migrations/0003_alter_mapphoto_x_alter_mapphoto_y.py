# Generated by Django 4.2.7 on 2023-11-23 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapphotos', '0002_alter_mapphoto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapphoto',
            name='x',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mapphoto',
            name='y',
            field=models.FloatField(),
        ),
    ]