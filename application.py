from config import default_base_path
from core.library_management import photo_search
from utilities.image import get_path_keys

middleware = [get_path_keys]

found = photo_search(default_base_path, middleware)

for photo in found:
    print(photo)
