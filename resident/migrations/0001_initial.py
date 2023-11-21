# Generated by Django 4.2.7 on 2023-11-21 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2500)),
                ('direction', models.CharField(choices=[('it', 'ИТ'), ('prod', 'производство'), ('energ', 'энергоэффективность'), ('bio', 'биотехнологии'), ('build', 'строительство')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ResidentPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='resident_photos')),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='resident.resident')),
            ],
        ),
    ]
