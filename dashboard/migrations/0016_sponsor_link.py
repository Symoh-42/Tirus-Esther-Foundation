# Generated by Django 4.1.7 on 2024-04-19 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_alter_settings_objectives'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
