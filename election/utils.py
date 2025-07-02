from PIL import Image, ExifTags
import os
import tempfile

def correct_image_orientation(image_path):
    try:
        image = Image.open(image_path)

        # Convert RGBA or P mode images to RGB
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        # Try to find orientation EXIF tag
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        exif = image._getexif()

        if exif is not None:
            orientation_value = exif.get(orientation, None)

            if orientation_value == 3:
                image = image.rotate(180, expand=True)
            elif orientation_value == 6:
                image = image.rotate(270, expand=True)
            elif orientation_value == 8:
                image = image.rotate(90, expand=True)

        # Save corrected image to a temp file
        tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
        image.save(tmp_file.name, format='JPEG')
        return tmp_file.name

    except Exception as e:
        print("🔴 Orientation correction failed:", e)
        return None
