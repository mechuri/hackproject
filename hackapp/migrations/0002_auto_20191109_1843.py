# Generated by Django 2.2.7 on 2019-11-09 09:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='liked_users', to=settings.AUTH_USER_MODEL),
        ),
    ]