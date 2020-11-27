# Library management utilities

from pathlib import Path
from os import listdir
from utilities import get_extension
from config import image_extensions
from core.Photo import Photo


def photo_search(base_path, middleware=None):
    """
    Searches for images within the provided base directory

    :param Path base_path: Path of the base directory to perform search in
    :param list middleware: List of middleware functions to apply to the identified photos
    :return list[Photo]: List of paths to images
    """
    if middleware is None:
        middleware = []

    photos = []
    to_search = [Path(base_path)]

    while len(to_search) > 0:
        current_base = to_search.pop()

        for child in listdir(current_base):
            child = current_base / Path(child)

            if child.is_dir():
                to_search.append(child)
                continue

            extension = get_extension(child)
            if extension is None:
                continue
            elif extension.lower() in image_extensions:
                new_photo = Photo(child)
                photos.append(new_photo)

                for ware in middleware:
                    ware(new_photo)

    return photos
