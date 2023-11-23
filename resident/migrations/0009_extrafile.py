# Generated by Django 4.2.7 on 2023-11-23 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0008_freeday_busyday'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.URLField()),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_files', to='resident.resident')),
            ],
        ),
    ]
