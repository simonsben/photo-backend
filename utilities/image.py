# Image utilities

from pathlib import Path
from re import compile
from config import default_base_path
from core.Photo import Photo

keyword_pattern = compile(r'[a-zA-Z]{3,}|[0-9]{4}(?=[^\w\d])')
extension_pattern = compile(r'(.*)\.\w+$')
default_base_memberships = set(default_base_path.split('\\'))


def get_path_keys(photo):
    """
    Extracts path keywords from photo path

    :param Photo photo:
    :param Path base_path:
    """
    photo_path = photo.path.name

    without_extension = extension_pattern.search(photo_path)[1]
    photo.add_keywords(keyword_pattern.findall(without_extension))


def directory_memberships(photo, base_memberships=None):
    """
    Compute the directory-based memberships of the photo (i.e. which albums they're in)

    :param Photo photo: Photo
    :param set base_memberships: Set of memberships of the base directory
    """
    if base_memberships is None:
        base_memberships = default_base_memberships

    photo_memberships = set(str(photo.path).split('\\')[:-1])

    photo.memberships.update(photo_memberships - base_memberships)
