# Generated by Django 2.2.7 on 2019-11-09 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackapp', '0003_challenge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenge',
            old_name='make',
            new_name='inherit',
        ),
    ]
