from config import base_path
from core.library_management import photo_search
from utilities.image import get_path_keys

found = photo_search(base_path)[0]

print(get_path_keys(found, base_path))
