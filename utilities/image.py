# Image utilities
from pathlib import Path
from re import compile


split_key = compile('[\\\\/]')


def get_path_keys(path, base_path):
    if isinstance(path, Path):
        path = str(path)

    significant = path[len(base_path):]

    significant = [entry for entry in split_key.split(significant) if len(entry) > 0]

    return significant
