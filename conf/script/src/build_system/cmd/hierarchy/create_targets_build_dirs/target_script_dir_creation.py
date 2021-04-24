__all__ = ['create_targets_script_dirs']

from build_system.build_target import *
from ..consts import *


def create_targets_script_dirs(targets: list[CompilerInstanceTargets]) -> None:
    for targets_of_compiler_instance in targets:
        for build_target in targets_of_compiler_instance:
            _create_target_script_dir_of_compiler_instance(target_of_compiler_instance=build_target)


def _create_target_script_dir_of_compiler_instance(target_of_compiler_instance: BuildTarget) -> None:
    target_of_compiler_instance.script_dir = target_of_compiler_instance.dir / TARGET_SCRIPT_DIR_NAME
    target_of_compiler_instance.script_dir.mkdir(mode=BUILD_DIR_PERMISSIONS, exist_ok=True)
