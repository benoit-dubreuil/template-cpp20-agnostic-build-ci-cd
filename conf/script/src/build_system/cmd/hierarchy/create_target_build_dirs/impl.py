from pathlib import Path
from typing import Optional

import utils.error.cls_def
import utils.more_path


def _assure_build_dir_exists(build_dir_cli_arg):
    import build_system.cmd.hierarchy.create_build_dir

    if build_dir_cli_arg is None:
        build_dir_cli_arg = build_system.cmd.hierarchy.create_build_dir.create_build_dir()
    else:
        if not build_dir_cli_arg.exists():
            raise utils.error.cls_def.BuildDirNotFoundError()

    return build_dir_cli_arg


def _assure_build_dir_is_empty(build_dir):
    if not utils.more_path.is_dir_empty(build_dir):
        raise utils.error.cls_def.BuildDirNotEmptyError()


def _generate_target_build_dir_names():
    import build_system.cmd.hierarchy.create_target_build_dirs.target_dir_name_generation

    target_build_dir_names = build_system.cmd.hierarchy.create_target_build_dirs.target_dir_name_generation.generate_target_build_dir_names()

    if len(target_build_dir_names) <= 0:
        raise utils.error.cls_def.NoSupportedCompilersAvailableError()

    return target_build_dir_names


def _create_all_target_build_dirs(build_dir):
    import build_system.cmd.hierarchy.create_target_build_dirs.target_dir_creation

    target_build_dir_names = _generate_target_build_dir_names()
    return build_system.cmd.hierarchy.create_target_build_dirs.target_dir_creation.create_all_target_build_dirs(build_dir, target_build_dir_names)


def create_target_build_dirs(build_dir: Optional[Path] = None) -> list[Path]:
    build_dir = _assure_build_dir_exists(build_dir)
    _assure_build_dir_is_empty(build_dir)

    return _create_all_target_build_dirs(build_dir)
