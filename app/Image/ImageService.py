import hashlib
import logging
import os

from PIL import Image
from fastapi.responses import FileResponse
from sqlalchemy.exc import IntegrityError

IMAGE_FOLDER = '../images/'


def get_image_file_path(image_name):
    return os.path.join(IMAGE_FOLDER, image_name)


def get_image(image_name):
    image_disk_path = get_image_file_path(image_name)
    if not os.path.exists(image_disk_path):
        return FileResponse(get_image_file_path('notfound.jpg'))

    return FileResponse(image_disk_path)


def resize_image(image):
    image = Image.open(image)
    image.thumbnail([800, 600], Image.ANTIALIAS)

    return image


def save_image_to_disk(image):
    file_name = hashlib.md5(image.tobytes()).hexdigest() + '.jpg'

    image_file_path = os.path.join('../images/', file_name)
    if not os.path.exists(image_file_path):
        image.save(image_file_path, 'JPEG')

    return file_name


def save_image(item_id, model, image, db):
    image = resize_image(image.file)
    image_file_namea = save_image_to_disk(image)

    db_item = model(item_id=item_id, image=image_file_namea)

    db.add(db_item)

    try:
        db.commit()
        db.refresh(db_item)
    except IntegrityError:
        logging.warning('Image already exists: %s', image_file_namea)
        db.rollback()

    return db_item
