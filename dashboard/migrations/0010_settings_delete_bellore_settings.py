# Generated by Django 4.1.7 on 2024-02-15 07:43

from django.db import migrations, models
import django_resized.forms
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_bellore_settings_main_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('phone', models.CharField(blank=True, max_length=300, null=True)),
                ('phone2', models.CharField(blank=True, max_length=300, null=True)),
                ('location', models.CharField(blank=True, max_length=300, null=True)),
                ('google_map', models.CharField(blank=True, max_length=500, null=True)),
                ('mail_account', models.CharField(blank=True, max_length=300, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('vision', models.TextField(blank=True, null=True)),
                ('mission', models.TextField(blank=True, null=True)),
                ('core', models.TextField(blank=True, null=True)),
                ('facebook', models.CharField(blank=True, max_length=300, null=True)),
                ('tiktok', models.CharField(blank=True, max_length=300, null=True)),
                ('instagram', models.CharField(blank=True, max_length=300, null=True)),
                ('twitter', models.CharField(blank=True, max_length=300, null=True)),
                ('youtube', models.CharField(blank=True, max_length=300, null=True)),
                ('pinterest', models.CharField(blank=True, max_length=300, null=True)),
                ('main_logo', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=90, scale=None, size=[1920, 1080], upload_to='logo/')),
            ],
            options={
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.DeleteModel(
            name='Bellore_Settings',
        ),
    ]
