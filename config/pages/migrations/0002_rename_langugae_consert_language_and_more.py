# Generated by Django 4.2.3 on 2023-07-27 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consert',
            old_name='langugae',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='langugae',
            new_name='language',
        ),
    ]
