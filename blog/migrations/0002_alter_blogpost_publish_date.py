# Generated by Django 4.1.7 on 2024-02-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
