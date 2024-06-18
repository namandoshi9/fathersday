# Generated by Django 5.0.6 on 2024-06-12 07:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0006_remove_upload_image_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload_image',
            name='merged_image',
        ),
        migrations.RemoveField(
            model_name='upload_image',
            name='original_image',
        ),
        migrations.AddField(
            model_name='upload_image',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload_image',
            name='merged_image_path',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]