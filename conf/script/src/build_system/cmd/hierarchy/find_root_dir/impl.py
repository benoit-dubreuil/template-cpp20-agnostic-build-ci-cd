from pathlib import Path

import ext.error.core.cls_def
import ext.error.utils.try_external_errors
from build_system.cmd.hierarchy.consts import BUILD_SYSTEM_CONF_FILE_NAME


def is_dir_root(root_dir: Path) -> bool:
    assert root_dir.is_dir()

    build_system_conf_file = root_dir / BUILD_SYSTEM_CONF_FILE_NAME
    return build_system_conf_file.is_file()


def _walk_parent_path(current_path: Path = Path()) -> (Path, Path):
    ext.error.utils.try_external_errors.try_manage_strict_path_resolving(path_to_resolve=current_path,
                                                                         external_errors_to_manage={(Exception,): ext.error.core.cls_def.RootDirNotFoundError})

    last_path = current_path
    current_path = current_path.parent

    return current_path, last_path


def find_root_dir() -> Path:
    current_path, last_path = _walk_parent_path(Path().absolute())
    is_last_path_root_dir = is_dir_root(last_path)

    while current_path != last_path and not is_last_path_root_dir:
        is_last_path_root_dir = is_dir_root(current_path)
        current_path, last_path = _walk_parent_path(current_path)

    if not is_last_path_root_dir:
        raise ext.error.core.cls_def.RootDirNotFoundError()

    return last_path
