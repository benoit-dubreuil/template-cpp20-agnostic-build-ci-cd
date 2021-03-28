from pathlib import Path
from typing import Optional

import build_system.cmd.hierarchy.assure_arg_integrity


def _recreate_build_dir(root_dir: Optional[Path] = None) -> Path:
    import build_system.cmd.hierarchy.clean_build_dir
    import build_system.cmd.hierarchy.create_build_dir
    import build_system.cmd.hierarchy.find_build_dir

    build_dir = build_system.cmd.hierarchy.find_build_dir.get_build_dir_path_relative_to_root_dir(root_dir=root_dir)
    build_system.cmd.hierarchy.clean_build_dir.clean_build_dir(build_dir=build_dir, ignore_errors=True)
    build_dir = build_system.cmd.hierarchy.create_build_dir.create_build_dir(root_dir=root_dir)

    return build_dir


def _create_target_build_dirs(root_dir: Optional[Path] = None, supported_installed_compilers=None) -> list[Path]:
    import build_system.cmd.hierarchy.create_target_build_dirs

    root_dir = build_system.cmd.hierarchy.assure_arg_integrity.assure_root_dir_exists(root_dir=root_dir)
    build_dir = _recreate_build_dir(root_dir)
    target_build_dirs = build_system.cmd.hierarchy.create_target_build_dirs.create_target_build_dirs(build_dir=build_dir,
                                                                                                     supported_installed_compilers=supported_installed_compilers)

    return target_build_dirs


def setup_build_system(root_dir: Optional[Path] = None):
    import build_system.compiler.installed_instance
    import build_system.compiler.supported_installed_instances

    host_compilers: list[build_system.compiler.installed_instance.CompilerInstance] = build_system.compiler.supported_installed_instances.fetch_all()
    target_build_dirs: list[Path] = _create_target_build_dirs(root_dir=root_dir, supported_installed_compilers=host_compilers)

    # TODO : Execute this inside a 'Visual Studio 2019 Developer Command Prompt' for MSVC
    # Voir C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build
    # %comspec% /k "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
    import sys
    import os
    import subprocess

    env_vars_before = os.environ

    timeout_in_seconds: float = 20
    subprocess.run(shell=True, stderr=sys.stderr, check=True, timeout=timeout_in_seconds)

    env_vars_after = os.environ

    # TODO : WIP
    import mesonbuild.mesonmain

    current_package_path = Path(__file__).parent
    current_package_path.resolve(strict=True)
    current_package_path = current_package_path.absolute()

    meson_launcher: str = str(current_package_path)
    meson_cli_args: list[str] = ['-h']

    mesonbuild.mesonmain.run(meson_cli_args, meson_launcher)
