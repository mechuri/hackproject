# Generated by Django 2.2.7 on 2019-11-09 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hackapp', '0002_auto_20191109_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='img/')),
                ('make', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenge', to='hackapp.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]