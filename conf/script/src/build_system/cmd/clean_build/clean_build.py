import shutil
from pathlib import Path
from typing import Optional, Callable

import build_system.cmd.hierarchy.find_root


def clean_build(root: Optional[Path] = None, ignore_errors=False) -> bool:
    has_successfuly_cleaned_build = True

    build_system.cmd.hierarchy.find_root.find_root()

    # TODO
    def _on_rmtree_error(function: Callable, path: str, excinfo: str):
        nonlocal has_successfuly_cleaned_build
        has_successfuly_cleaned_build = False

    return False  # TODO
