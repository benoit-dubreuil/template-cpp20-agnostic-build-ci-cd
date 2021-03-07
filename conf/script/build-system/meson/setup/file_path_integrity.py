from pathlib import Path


def assure_file_path_integrity(file_path: Path):
    if not file_path.exists() or not file_path.is_file():
        if file_path.is_dir():
            raise IsADirectoryError()
        raise FileNotFoundError()
