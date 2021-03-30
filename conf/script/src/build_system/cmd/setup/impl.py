from pathlib import Path
from typing import Optional

import mesonbuild.mesonmain

import build_system.build_target.compiler_instance_targets
import build_system.compiler.installed_instance
import build_system.compiler.installed_instance.msvc
import build_system.compiler.supported_installed_instances
from build_system.cmd.setup.create_targets_dirs import _create_all_compiler_instances_targets_build_dirs


def setup_build_system(root_dir: Optional[Path] = None):
    # TODO : Foreach compiler, foreach target build dir...
    host_compilers = build_system.compiler.supported_installed_instances.fetch_all()
    target_build_dirs = _create_all_compiler_instances_targets_build_dirs(root_dir=root_dir,
                                                                          supported_installed_compilers=host_compilers)

    # TODO : WIP
    meson_launcher: str = _fetch_meson_launcher()
    meson_cli_args: list[str] = ['-h']

    mesonbuild.mesonmain.run(meson_cli_args, meson_launcher)


def _setup_host_compiler_all_target_build_dirs(host_compiler: build_system.compiler.installed_instance.CompilerInstance,
                                               target_build_dirs: list[Path]):
    if host_compiler.requires_env_vars_setup():
        host_compiler.setup_env_vars()

    for target in target_build_dirs:
        _setup_host_compiler_target_build_dir(host_compiler=host_compiler, target_build_dir=target)

    if host_compiler.requires_env_vars_setup():
        host_compiler.teardown_env_vars()


def _setup_host_compiler_target_build_dir(host_compiler: build_system.compiler.installed_instance.CompilerInstance,
                                          target_build_dir: Path):
    # TODO
    ...


def _fetch_meson_launcher() -> str:
    current_package_path = _fetch_current_package_path()
    return str(current_package_path)


def _fetch_current_package_path() -> Path:
    current_package_path = Path(__file__).parent
    current_package_path.resolve(strict=True)
    current_package_path = current_package_path.absolute()

    return current_package_path
