# Generated by Django 5.0.6 on 2024-06-12 09:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0010_alter_upload_image_merged_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload_image',
            name='image',
        ),
        migrations.AddField(
            model_name='upload_image',
            name='original_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='original_images/'),
            preserve_default=False,
        ),
    ]
