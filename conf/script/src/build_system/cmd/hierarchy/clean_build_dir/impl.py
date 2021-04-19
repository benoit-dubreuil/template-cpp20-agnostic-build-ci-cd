import shutil
from pathlib import Path
from typing import Optional

import build_system.cmd.hierarchy.assure_arg_integrity
import ext.error.core.cls_def
import ext.error.core.managed


def clean_build_dir(build_dir: Optional[Path] = None, ignore_errors=False) -> bool:
    import build_system.cmd.hierarchy.find_build_dir

    has_successfuly_cleaned_build = True

    def _on_rmtree_error(function, path, excinfo):
        nonlocal has_successfuly_cleaned_build
        has_successfuly_cleaned_build = False

    try:
        build_dir = build_system.cmd.hierarchy.assure_arg_integrity.get_verified_build_dir(unverified_build_dir=build_dir)

    except ext.error.core.managed.ManagedErrorMixin as raised_error:
        if not ignore_errors:
            raise raised_error

    if build_dir is not None:
        shutil.rmtree(build_dir, ignore_errors, _on_rmtree_error)

    return (build_dir is not None) and has_successfuly_cleaned_build
