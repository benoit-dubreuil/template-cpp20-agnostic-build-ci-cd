from pathlib import Path
from typing import Optional

import build_system.cmd.hierarchy.assure_arg_integrity
import build_system.compiler.installed_instance
import utils.error.cls_def
import utils.more_path


def _assure_build_dir_is_empty(build_dir):
    if not utils.more_path.is_dir_empty(build_dir):
        raise utils.error.cls_def.BuildDirNotEmptyError()


def _generate_target_build_dir_names(supported_installed_compilers: Optional[list[build_system.compiler.installed_instance.CompilerInstance]] = None):
    import build_system.cmd.hierarchy.create_target_build_dirs.target_dir_name_generation

    target_build_dir_names = build_system.cmd.hierarchy.create_target_build_dirs.target_dir_name_generation.generate_target_build_dir_names(
        supported_installed_compilers=supported_installed_compilers)

    if len(target_build_dir_names) <= 0:
        raise utils.error.cls_def.NoSupportedCompilersAvailableError()

    return target_build_dir_names


def _create_all_target_build_dirs(build_dir: Path,
                                  supported_installed_compilers: Optional[list[build_system.compiler.installed_instance.CompilerInstance]] = None) \
        -> list[(Path, build_system.compiler.installed_instance.CompilerInstance)]:
    import build_system.cmd.hierarchy.create_target_build_dirs.target_dir_creation

    target_build_dir_names = _generate_target_build_dir_names(supported_installed_compilers=supported_installed_compilers)
    return build_system.cmd.hierarchy.create_target_build_dirs.target_dir_creation.create_all_target_build_dirs(build_dir, target_build_dir_names)


def create_target_build_dirs(build_dir: Optional[Path] = None,
                             supported_installed_compilers: Optional[list[build_system.compiler.installed_instance.CompilerInstance]] = None) \
        -> list[(Path, build_system.compiler.installed_instance.CompilerInstance)]:
    build_dir = build_system.cmd.hierarchy.assure_arg_integrity.assure_build_dir_exists(build_dir=build_dir)
    _assure_build_dir_is_empty(build_dir)

    return _create_all_target_build_dirs(build_dir, supported_installed_compilers=supported_installed_compilers)
