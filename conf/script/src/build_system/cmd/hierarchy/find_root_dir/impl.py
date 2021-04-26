__all__ = ['get_build_system_conf_file_path',
           'verify_root_dir_accessibility',
           'verify_root_path_is_dir',
           'verify_dir_is_a_root_dir',
           'is_dir_a_root_dir',
           'find_root_dir',
           'find_or_verify_root_dir']

from pathlib import Path
from typing import Optional

from ext.error import *
from ext.error.utils import *
from file_structure import *


def get_build_system_conf_file_path(root_dir: Path) -> Path:
    return root_dir / BUILD_SYSTEM_CONF_FILE_NAME


def verify_root_dir_accessibility(root_dir: Path):
    try_manage_strict_path_resolving(path_to_resolve=root_dir,
                                     external_errors_to_manage={(Exception,): RootDirNotFoundError})


def verify_root_path_is_dir(root_dir: Path):
    if not root_dir.is_dir():
        raise RootDirNotDirError()


def _verify_build_system_conf_file(build_system_conf_file: Path):
    try_manage_strict_path_resolving(path_to_resolve=build_system_conf_file,
                                     external_errors_to_manage={(Exception,): RootDirMissingBuildSystemConfFileError})

    if not build_system_conf_file.is_file():
        raise RootDirMissingBuildSystemConfFileError()


def verify_dir_is_a_root_dir(root_dir: Path):
    """
    Verifies that the supplied directory is a root directory by testing if it contains a build system configuration file.

    The build system configuration file name is queried from :func:`~get_build_system_conf_file_path`.

    :param root_dir: The directory to test on. It must exist, be accessible and be a directory. No verifications are done for those requirements.
    :type root_dir: Path
    :raises RootDirMissingBuildSystemConfFileError: * if the root_dir does not contains a build system configuration file
                                                    * if the build system configuration file is not actually a file.
    """

    build_system_conf_file = get_build_system_conf_file_path(root_dir=root_dir)
    _verify_build_system_conf_file(build_system_conf_file=build_system_conf_file)


def is_dir_a_root_dir(root_dir: Path) -> bool:
    """
    Checks if the supplied directory is a root directory by testing if it contains a build system configuration file.

    The build system configuration file name is queried from :func:`~get_build_system_conf_file_path`.

    :param root_dir: The directory to test on. It must exist, be accessible and be a directory. No verifications are done for those requirements.
    :type root_dir: Path
    :return: :const:`True` if the supplied directory is a root directory, :const:`False` otherwise.
    :rtype: bool
    """

    has_build_system_conf_file: bool

    try:
        verify_dir_is_a_root_dir(root_dir=root_dir)
        has_build_system_conf_file = True
    except RootDirMissingBuildSystemConfFileError:
        has_build_system_conf_file = False

    return has_build_system_conf_file


def _walk_parent_path(current_path: Path = Path()) -> (Path, Path):
    verify_root_dir_accessibility(root_dir=current_path)

    last_path = current_path
    current_path = current_path.parent

    return current_path, last_path


def find_root_dir() -> Path:
    current_path = Path().absolute()

    current_path, last_path = _walk_parent_path(current_path)
    is_last_path_root_dir = is_dir_a_root_dir(root_dir=last_path)

    while current_path != last_path and not is_last_path_root_dir:
        current_path, last_path = _walk_parent_path(current_path=current_path)
        is_last_path_root_dir = is_dir_a_root_dir(root_dir=last_path)

    if not is_last_path_root_dir:
        raise RootDirNotFoundError()

    return last_path


def find_or_verify_root_dir(unverified_root_dir: Optional[Path] = None) -> Path:
    root_dir: Path

    if unverified_root_dir is None:
        root_dir = find_root_dir()
    else:
        verify_root_dir_accessibility(root_dir=unverified_root_dir)
        verify_root_path_is_dir(root_dir=unverified_root_dir)
        verify_dir_is_a_root_dir(root_dir=unverified_root_dir)

        root_dir = unverified_root_dir

    return root_dir
