from core.library_management import photo_search
from utilities.image import get_path_keys, directory_memberships

default_middleware = [get_path_keys, directory_memberships]


class Library:
    """ Class to enable easy in-memory management of the library """
    def __init__(self, location, middleware=None):
        self.location = location

        if middleware is None:
            middleware = default_middleware
        self.photos = photo_search(location, middleware)

    def __str__(self):
        """ Overrides the default __str__ method """
        output = 'Library: \n'
        output += '\n'.join((str(photo) for photo in self.photos))

        return output
