from pathlib import Path
from os import listdir
from utilities import get_extension
from config import image_extensions


def photo_search(base_path):
    """
    Searches for images within the provided base directory

    :param Path base_path: Path of the base directory to perform search in
    :return list[Path]: List of paths to images
    """

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
            elif extension in image_extensions:
                photos.append(child)

    return photos
