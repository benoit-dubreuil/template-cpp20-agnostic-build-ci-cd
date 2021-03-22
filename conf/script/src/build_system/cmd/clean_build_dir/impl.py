import shutil
from pathlib import Path
from typing import Optional

import utils.error.managed


def clean_build_dir(root_dir: Optional[Path] = None, ignore_errors=False) -> bool:
    import build_system.cmd.hierarchy.find_build_dir

    # noinspection PyUnusedLocal
    def _on_rmtree_error(function, path, excinfo):
        nonlocal has_successfuly_cleaned_build
        has_successfuly_cleaned_build = False

    has_successfuly_cleaned_build = True
    build_dir: Optional[Path] = None

    try:
        build_dir = build_system.cmd.hierarchy.find_build_dir.find_build_dir(root_dir)

    except utils.error.managed.ManagedErrorMixin as raised_error:
        if not ignore_errors:
            raise raised_error

    if build_dir is not None:
        shutil.rmtree(build_dir, ignore_errors, _on_rmtree_error)

    return (build_dir is not None) and has_successfuly_cleaned_build
