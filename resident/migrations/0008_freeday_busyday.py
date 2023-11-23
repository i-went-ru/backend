# Generated by Django 4.2.7 on 2023-11-23 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0007_alter_resident_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='free_days', to='resident.resident')),
            ],
        ),
        migrations.CreateModel(
            name='BusyDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='busy_days', to='resident.resident')),
            ],
        ),
    ]