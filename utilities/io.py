# I/O utilities
from pathlib import Path


def make_path(_path):
    return Path(_path)


def get_extension(path):
    if not isinstance(path, Path):
        path = Path(path)

    extension = path.suffix
    if extension == '':
        return None
    return extension[1:]


def check_existence(**paths):
    """
    Checks if the provided paths exist

    :param list[str, Path] paths:
    """
    for path in paths:
        if not isinstance(path, Path):      # If not of type Path, cast
            path = Path(path)

        if not path.exists():               # Check if file exists
            raise FileExistsError(path)
