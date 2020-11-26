# Image utilities
from pathlib import Path
from re import compile
from config import default_base_path
from core.Photo import Photo

keyword_pattern = compile(r'[a-zA-Z]{3,}|[0-9]{4}(?=[^\w\d])')
extension_pattern = compile(r'(.*)\.\w+$')


def get_keywords(matches):
    return [str(match) for match in matches]


def get_path_keys(photo, base_path=default_base_path):
    """
    Extracts path keywords from photo path

    :param Photo photo:
    :param Path base_path:
    """
    photo_path = str(photo.path)
    without_base_path = photo_path[len(str(base_path)):]

    without_extension = extension_pattern.search(without_base_path)[1]
    photo.add_keywords(keyword_pattern.findall(without_extension))
