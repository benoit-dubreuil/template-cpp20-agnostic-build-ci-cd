__all__ = ['clean_build_dir']

import shutil
from pathlib import Path
from typing import Optional

from ext.error import *
from ..assure_arg_integrity import *


def clean_build_dir(build_dir: Optional[Path] = None, ignore_errors=False) -> bool:
    has_successfuly_cleaned_build = True

    def _on_rmtree_error(function, path, excinfo):
        nonlocal has_successfuly_cleaned_build
        has_successfuly_cleaned_build = False

    try:
        build_dir = get_verified_build_dir(unverified_build_dir=build_dir)

    except ManagedErrorMixin as raised_error:
        if not ignore_errors:
            raise raised_error

    if build_dir is not None:
        shutil.rmtree(build_dir, ignore_errors, _on_rmtree_error)

    return (build_dir is not None) and has_successfuly_cleaned_build
