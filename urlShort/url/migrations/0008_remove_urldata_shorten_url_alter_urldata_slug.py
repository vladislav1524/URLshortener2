# Generated by Django 5.0.7 on 2024-08-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0007_urldata_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urldata',
            name='shorten_url',
        ),
        migrations.AlterField(
            model_name='urldata',
            name='slug',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
