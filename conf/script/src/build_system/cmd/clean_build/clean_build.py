import shutil
from pathlib import Path
from typing import Optional, Callable, Final

import build_system.cmd.hierarchy.find_root

BUILD_DIR_NAME: Final[str] = 'build'


def clean_build(root: Optional[Path] = None, ignore_errors=False) -> bool:
    has_successfuly_cleaned_build = True

    if root is None:
        root = build_system.cmd.hierarchy.find_root.find_root()

    # TODO
    def _on_rmtree_error(function: Callable, path: str, excinfo: str):
        nonlocal has_successfuly_cleaned_build
        has_successfuly_cleaned_build = False

    return False  # TODO
