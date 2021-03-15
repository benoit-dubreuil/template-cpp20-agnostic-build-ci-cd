import shutil
from pathlib import Path
from typing import Optional

import build_system.cmd.hierarchy.find_build_dir
from build_system import cmd


def clean_build_dir(root_dir: Optional[Path] = None, ignore_errors=False) -> bool:
    # noinspection PyUnusedLocal
    def _on_rmtree_error(function, path, excinfo):
        nonlocal has_successfuly_cleaned_build
        has_successfuly_cleaned_build = False

    has_successfuly_cleaned_build = True
    build_dir: Optional[Path] = None

    try:
        build_dir = cmd.hierarchy.find_build_dir.find_build_dir(root_dir)
    except OSError as raised_exception:
        if not ignore_errors:
            raise raised_exception

    if build_dir is not None:
        shutil.rmtree(build_dir, ignore_errors, _on_rmtree_error)

    return (build_dir is not None) and has_successfuly_cleaned_build
