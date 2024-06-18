from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Upload_image
import base64
from django.core.files.base import ContentFile
from PIL import Image, ImageOps
from io import BytesIO
import os
from django.conf import settings  # Import the settings module
from django.http import FileResponse


def index(request):
    image_url = None
    success_message = None
    name = None  # Set a default value for 'name'
    if request.method == 'POST':
        name = request.POST.get('name')
        original_image = request.FILES.get('image')
        cropped_image = request.POST.get('cropped_image')

        if not name or not cropped_image:
            error_msg_name = "Name fields are required."
            error_msg_image = "Image fields are required."
            return render(request, 'today/index.html', {'error_msg_name': error_msg_name, 'error_msg_image': error_msg_image})
        else:
            # Decode the base64 image data
            format, imgstr = cropped_image.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'{name}.{ext}')
            
            # Save the original image
            original_instance = Upload_image(name=name, original_image=original_image, created_at=datetime.now())
            original_instance.save()
            
            # Save the uploaded image temporarily to merge with frame
            temp_image = Image.open(data)
            
            # Open the frame image
            frame_path = os.path.join(settings.STATICFILES_DIRS[0], 'images/frame.png')
            frame_image = Image.open(frame_path).convert("RGBA")
            
            # Resize the uploaded image to match the frame size (adjust size if necessary)
            temp_image = ImageOps.fit(temp_image, frame_image.size, Image.LANCZOS).convert("RGBA")
            
            # Merge the uploaded image with the frame
            merged_image = Image.alpha_composite(temp_image, frame_image)
            
            # Save the merged image to a BytesIO object
            merged_io = BytesIO()
            merged_image.save(merged_io, format='PNG')
            merged_content = ContentFile(merged_io.getvalue(), name=f'merged_{name}.png')
            
            # Save the merged image
            original_instance.merged_image.save(f'merged_{name}.png', merged_content)

            # Pass the image URL to the template
            image_url = original_instance.merged_image.url
            success_message = "Form submitted successfully!"
    
    return render(request, 'today/index.html', {'image_url': image_url, 'success_message': success_message, 'name': name})



def download_image(request, filename):
    # Retrieve the latest image with the given name
    latest_image = Upload_image.objects.filter(name=filename).order_by('-created_at').first()

    if latest_image:
        # Serve the latest image as a file response with the desired filename
        response = FileResponse(latest_image.merged_image, as_attachment=True, filename=f'{filename}.png')
        return response
    else:
        # If no image with the given name is found, return a 404 response
        return HttpResponse("Image not found.", status=404)
