# Generated by Django 4.2 on 2023-08-26 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myappone', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Description',
            new_name='description',
        ),
    ]
