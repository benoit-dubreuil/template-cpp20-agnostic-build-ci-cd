__all__ = ['create_targets_build_dirs_structure']

from pathlib import Path
from typing import Optional

from build_system.build_target import *
from build_system.compiler import *
from ext.error import *
from ext.more_path import *
from .target_dir_creation import *
from .target_dir_name_generation import *
from .target_script_dir_creation import *
from ..assure_arg_integrity import *


def create_targets_build_dirs_structure(build_dir: Optional[Path] = None,
                                        compiler_instances: Optional[list[CompilerInstance]] = None) \
        -> list[CompilerInstanceTargets]:
    build_dir = find_or_verify_build_dir(unverified_build_dir=build_dir)
    _assure_build_dir_is_empty(build_dir)

    return _unchecked_create_targets_build_dirs(build_dir, compiler_instances=compiler_instances)


def _assure_build_dir_is_empty(build_dir):
    if not is_dir_empty(build_dir):
        raise BuildDirNotEmptyError()


def _unchecked_create_targets_build_dirs(build_dir: Path,
                                         compiler_instances: Optional[list[CompilerInstance]] = None) \
        -> list[CompilerInstanceTargets]:
    targets = generate_targets(compiler_instances=compiler_instances)

    create_targets_build_dirs(build_dir=build_dir, targets=targets)
    create_targets_script_dirs(targets=targets)

    return targets
