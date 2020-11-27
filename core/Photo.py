from pathlib import Path


class Photo:
    """ Class to wrap photos for easier management """
    def __init__(self, path: Path):
        self.path = Path(path)
        self.keywords = []
        self.memberships = set()

    def add_keywords(self, keywords):
        """
        Adds keywords to list

        :param list[str] keywords: Keywords to add to photo
        """
        self.keywords += keywords

    def __str__(self):
        """ Overrides the default __str__ method """
        path = self.path.name

        return '%s => %s' % (path, str(self.memberships))
