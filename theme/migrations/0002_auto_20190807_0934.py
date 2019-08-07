# Generated by Django 2.2.1 on 2019-08-07 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theme', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='last_modified_user_id',
        ),
        migrations.AddField(
            model_name='theme',
            name='last_modified_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='theme_last_modified_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
