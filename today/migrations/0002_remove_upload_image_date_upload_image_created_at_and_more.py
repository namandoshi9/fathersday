# Generated by Django 5.0.6 on 2024-06-12 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload_image',
            name='date',
        ),
        migrations.AddField(
            model_name='upload_image',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='upload_image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
