# Generated by Django 4.0.2 on 2022-02-26 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cykl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cykl_users',
            name='username',
        ),
        migrations.AddField(
            model_name='cykl_users',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]