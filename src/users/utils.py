import os, secrets
from PIL import Image
from flask import current_app


def save_picture(form_image, output_size=(125, 125)):
    random_hex = secrets.token_hex(8)
    filename, file_extension = os.path.splitext(form_image.filename)
    image_filename = filename[:10] + random_hex + file_extension
    picture_path = os.path.join(current_app.root_path, "static", "profile_photos", image_filename)
    
    image = Image.open(form_image)
    image.thumbnail(output_size)
    image.save(picture_path)
    
    return image_filename
