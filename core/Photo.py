from pathlib import Path


class Photo:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.keywords = []

    def add_keywords(self, keywords):
        """
        Adds keywords to list

        :param list[str] keywords: Keywords to add to photo
        """
        self.keywords += keywords

    def __str__(self):
        path = self.path.name

        return '%s => %s' % (path, str(self.keywords))
