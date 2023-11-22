# Generated by Django 4.2.7 on 2023-11-22 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField(unique=True)),
                ('status', models.CharField(choices=[('canceled', 'canceled'), ('moderation', 'moderation'), ('approved', 'approved'), ('notapproved', 'notapproved')], max_length=11)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours', to=settings.AUTH_USER_MODEL)),
                ('guide', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guided_tours', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
