# Generated by Django 4.2.11 on 2024-03-24 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='url',
        ),
    ]
