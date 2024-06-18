from django.db import models
from datetime import datetime

class Upload_image(models.Model):
    name = models.CharField(max_length=100)
    original_image = models.ImageField(upload_to='original_images/')
    merged_image = models.ImageField(upload_to='merged_images/', blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
