from pathlib import Path
from typing import Optional

import build_system.build_target.compiler_instance_targets
import build_system.cmd.hierarchy.assure_arg_integrity
import build_system.compiler.installed_instance
import utils.error.core.cls_def
import utils.more_path


def create_targets_build_dirs(build_dir: Optional[Path] = None,
                              compiler_instances: Optional[list[build_system.compiler.installed_instance.CompilerInstance]] = None) \
        -> list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]:
    build_dir = build_system.cmd.hierarchy.assure_arg_integrity.get_verified_build_dir(unverified_build_dir=build_dir)
    _assure_build_dir_is_empty(build_dir)

    return _unchecked_create_targets_build_dirs(build_dir, compiler_instances=compiler_instances)


def _assure_build_dir_is_empty(build_dir):
    if not utils.more_path.is_dir_empty(build_dir):
        raise utils.error.core.cls_def.BuildDirNotEmptyError()


def _unchecked_create_targets_build_dirs(build_dir: Path,
                                         compiler_instances: Optional[list[build_system.compiler.installed_instance.CompilerInstance]] = None) \
        -> list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]:
    from build_system.cmd.hierarchy.create_targets_build_dirs.target_dir_name_generation import checked_generate_targets
    from build_system.cmd.hierarchy.create_targets_build_dirs.target_dir_creation import create_targets_build_dirs
    from build_system.cmd.hierarchy.create_targets_build_dirs.target_script_dir_creation import create_targets_script_dirs

    targets = checked_generate_targets(compiler_instances=compiler_instances)

    create_targets_build_dirs(build_dir=build_dir, targets=targets)
    create_targets_script_dirs(targets=targets)

    return targets
