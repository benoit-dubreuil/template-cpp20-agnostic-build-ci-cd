from pathlib import Path


def fetch_meson_launcher() -> str:
    current_package_path = _fetch_current_package_path()
    return str(current_package_path)


def _fetch_current_package_path() -> Path:
    current_package_path = Path(__file__).parent
    current_package_path.resolve(strict=True)
    current_package_path = current_package_path.absolute()

    return current_package_path
