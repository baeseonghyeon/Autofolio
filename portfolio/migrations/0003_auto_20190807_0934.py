# Generated by Django 2.2.1 on 2019-08-07 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190807_0640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='last_modified_user_id',
            new_name='last_modified_user',
        ),
        migrations.RenameField(
            model_name='subdomain',
            old_name='last_modified_user_id',
            new_name='last_modified_user',
        ),
    ]