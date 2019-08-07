# Generated by Django 2.2.3 on 2019-08-07 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('draft', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('use_yn', models.SmallIntegerField(default=1)),
                ('last_modified_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('draft_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draft.Draft')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subdomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_nm', models.TextField(max_length=100)),
                ('url', models.TextField(max_length=500)),
                ('last_modified_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('portfolio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Portfolio')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]