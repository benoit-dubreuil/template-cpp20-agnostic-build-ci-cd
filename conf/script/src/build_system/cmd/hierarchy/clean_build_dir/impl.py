import shutil
from pathlib import Path
from typing import Optional

import utils.error.managed
import utils.error.cls_def


def clean_build_dir(build_dir: Optional[Path] = None, ignore_errors=False) -> bool:
    import build_system.cmd.hierarchy.find_build_dir

    has_successfuly_cleaned_build = True

    # noinspection PyUnusedLocal
    def _on_rmtree_error(function, path, excinfo):
        nonlocal has_successfuly_cleaned_build
        has_successfuly_cleaned_build = False

    try:
        if build_dir is None:
            build_dir = build_system.cmd.hierarchy.find_build_dir.find_build_dir()
        else:
            if not build_dir.exists():
                raise utils.error.cls_def.BuildDirNotFoundError()

    except utils.error.managed.ManagedErrorMixin as raised_error:
        if not ignore_errors:
            raise raised_error

    if build_dir is not None:
        shutil.rmtree(build_dir, ignore_errors, _on_rmtree_error)

    return (build_dir is not None) and has_successfuly_cleaned_build
