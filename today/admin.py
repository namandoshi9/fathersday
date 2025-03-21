from django.contrib import admin
from .models import Upload_image  # Import your model

class images(admin.ModelAdmin):
    # Customize how your model is displayed in the admin interface
    list_display = ['name', 'original_image','merged_image', 'created_at']

# Register your model with the admin site
admin.site.register(Upload_image, images)
