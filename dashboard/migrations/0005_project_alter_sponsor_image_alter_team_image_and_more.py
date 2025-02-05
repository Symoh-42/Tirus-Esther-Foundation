# Generated by Django 4.1.7 on 2024-02-14 12:24

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_sponsor_sponsor_sponsor_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('main_image', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=90, scale=None, size=[1920, 1080], upload_to='project/')),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
                ('in_progress', models.BooleanField(blank=True, default=False, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default='default.jpg', force_format=None, keep_meta=True, quality=90, scale=None, size=[1920, 1080], upload_to='sponsor/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=90, scale=None, size=[1920, 1080], upload_to='team/'),
        ),
        migrations.CreateModel(
            name='OtherProductImages',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('other_project_images', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=90, scale=None, size=[1920, 1080], upload_to='products/')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.project')),
            ],
            options={
                'verbose_name_plural': 'Other project images',
            },
        ),
    ]
