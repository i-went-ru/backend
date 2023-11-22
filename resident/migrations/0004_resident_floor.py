# Generated by Django 4.2.7 on 2023-11-22 03:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0003_remove_resident_owner_resident_responsible_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='floor',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(12)]),
            preserve_default=False,
        ),
    ]