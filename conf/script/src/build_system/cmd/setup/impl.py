from pathlib import Path
from typing import Optional

import mesonbuild.mesonmain

import build_system.build_target.compiler_instance_targets
import build_system.cmd.hierarchy.assure_arg_integrity
import build_system.compiler.installed_instance
import build_system.compiler.installed_instance.msvc
import build_system.compiler.supported_installed_instances


def setup_build_system(root_dir: Optional[Path] = None):
    # TODO : Foreach compiler, foreach target build dir...
    host_compilers: list[build_system.compiler.installed_instance.CompilerInstance] = build_system.compiler.supported_installed_instances.fetch_all()
    target_build_dirs: list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets] = _create_target_build_dirs(root_dir=root_dir,
                                                                                                                                     supported_installed_compilers=host_compilers)

    # TODO : WIP
    meson_launcher: str = _fetch_meson_launcher()
    meson_cli_args: list[str] = ['-h']

    mesonbuild.mesonmain.run(meson_cli_args, meson_launcher)


def _create_target_build_dirs(root_dir: Optional[Path] = None,
                              supported_installed_compilers: Optional[list[build_system.compiler.installed_instance.compiler_instance]] = None) \
        -> list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]:
    import build_system.cmd.hierarchy.create_target_build_dirs

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
