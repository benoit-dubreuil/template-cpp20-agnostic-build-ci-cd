from pathlib import Path
from typing import Optional

import build_system.build_target.compiler_instance_targets
import build_system.compiler.installed_instance


def _create_all_compiler_instances_targets_build_dirs(root_dir: Optional[Path] = None,
                                                      supported_installed_compilers: Optional[list[build_system.compiler.installed_instance.compiler_instance]] = None) \
        -> list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]:
    import build_system.cmd.hierarchy.create_target_build_dirs
    import build_system.cmd.hierarchy.assure_arg_integrity

    root_dir = build_system.cmd.hierarchy.assure_arg_integrity.assure_root_dir_exists(root_dir=root_dir)
    build_dir = _recreate_build_dir(root_dir)
    target_build_dirs = build_system.cmd.hierarchy.create_target_build_dirs.create_target_build_dirs(build_dir=build_dir,
                                                                                                     supported_installed_compilers=supported_installed_compilers)

    return target_build_dirs


def _recreate_build_dir(root_dir: Optional[Path] = None) -> Path:
    import build_system.cmd.hierarchy.clean_build_dir
    import build_system.cmd.hierarchy.create_build_dir
    import build_system.cmd.hierarchy.find_build_dir

    build_dir = build_system.cmd.hierarchy.find_build_dir.get_build_dir_path_relative_to_root_dir(root_dir=root_dir)
    build_system.cmd.hierarchy.clean_build_dir.clean_build_dir(build_dir=build_dir, ignore_errors=True)
    build_dir = build_system.cmd.hierarchy.create_build_dir.create_build_dir(root_dir=root_dir)

    return build_dir
