# Generated by Django 4.2.6 on 2023-10-24 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Product',
        ),
    ]
