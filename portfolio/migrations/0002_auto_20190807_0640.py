# Generated by Django 2.2.3 on 2019-08-07 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='user_id',
            new_name='last_modified_user_id',
        ),
        migrations.RenameField(
            model_name='subdomain',
            old_name='user_id',
            new_name='last_modified_user_id',
        ),
    ]