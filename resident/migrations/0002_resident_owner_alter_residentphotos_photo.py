# Generated by Django 4.2.7 on 2023-11-21 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resident', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='residentphotos',
            name='photo',
            field=models.ImageField(upload_to='resident/photos'),
        ),
    ]
