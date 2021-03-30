from pathlib import Path
from typing import Optional

import build_system.build_target.compiler_instance_targets
import build_system.cmd.hierarchy.assure_arg_integrity
import build_system.compiler.installed_instance
import utils.error.cls_def
import utils.more_path


def create_target_build_dirs(build_dir: Optional[Path] = None,
                             supported_installed_compilers: Optional[list[build_system.compiler.installed_instance.CompilerInstance]] = None) \
        -> list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]:
    build_dir = build_system.cmd.hierarchy.assure_arg_integrity.assure_build_dir_exists(build_dir=build_dir)
    _assure_build_dir_is_empty(build_dir)

    return _create_all_compiler_instances_target_build_dirs(build_dir, supported_installed_compilers=supported_installed_compilers)


def _assure_build_dir_is_empty(build_dir):
    if not utils.more_path.is_dir_empty(build_dir):
        raise utils.error.cls_def.BuildDirNotEmptyError()


def _create_all_compiler_instances_target_build_dirs(build_dir: Path,
                                                     supported_installed_compilers: Optional[list[build_system.compiler.installed_instance.CompilerInstance]] = None) \
        -> list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]:
    import build_system.cmd.hierarchy.create_target_build_dirs.target_dir_creation

    all_compiler_instances_targets = _generate_all_compiler_instances_targets(supported_installed_compilers=supported_installed_compilers)
    build_system.cmd.hierarchy.create_target_build_dirs.target_dir_creation.create_all_compiler_instances_target_build_dirs(build_dir=build_dir,
                                                                                                                            all_compiler_instances_targets=all_compiler_instances_targets)

    return all_compiler_instances_targets


def _generate_all_compiler_instances_targets(supported_installed_compilers: Optional[list[build_system.compiler.installed_instance.CompilerInstance]] = None) \
        -> list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]:
    import build_system.cmd.hierarchy.create_target_build_dirs.target_dir_name_generation

    all_compiler_instances_targets = build_system.cmd.hierarchy.create_target_build_dirs.target_dir_name_generation.generate_all_compiler_instances_targets(
        supported_installed_compilers=supported_installed_compilers)

    if len(all_compiler_instances_targets) <= 0:
        raise utils.error.cls_def.NoSupportedCompilersAvailableError()

    return all_compiler_instances_targets
