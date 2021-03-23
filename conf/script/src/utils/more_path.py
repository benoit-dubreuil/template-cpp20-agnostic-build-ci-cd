import pathlib


def is_dir_empty(dir_path: pathlib.Path) -> bool:
    return not any(dir_path.iterdir())
