# Generated by Django 4.2.7 on 2023-11-22 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('guest', 'обыватель'), ('org', 'организация'), ('school', 'учебное заведение'), ('resident', 'резидент')], max_length=8),
        ),
    ]
