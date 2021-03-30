from pathlib import Path
from typing import Final, Optional

import mesonbuild.mesonmain

import build_system.build_target.build_target_cls
import build_system.build_target.compiler_instance_targets
import build_system.compiler.installed_instance
import build_system.compiler.installed_instance.msvc
import build_system.compiler.supported_installed_instances
from build_system.cmd.setup.create_targets_dirs import create_all_host_instances_targets_build_dirs
from build_system.cmd.setup.meson_utils import fetch_meson_launcher


def setup_build_system(root_dir: Optional[Path] = None):
    # TODO : Foreach compiler, foreach target build dir...
    host_compilers = build_system.compiler.supported_installed_instances.fetch_all()
    all_host_instances_targets = create_all_host_instances_targets_build_dirs(root_dir=root_dir,
                                                                              supported_installed_compilers=host_compilers)

    for host_instance_targets in all_host_instances_targets:
        ...

    # TODO : WIP
    meson_launcher: str = fetch_meson_launcher()
    meson_cli_args: list[str] = ['-h']

    mesonbuild.mesonmain.run(meson_cli_args, meson_launcher)


def _setup_host_compiler_all_target_build_dirs(host_compiler_targets: build_system.build_target.compiler_instance_targets.CompilerInstanceTargets):
    host_compiler: Final[build_system.compiler.installed_instance.CompilerInstance] = host_compiler_targets.compiler_instance

    if host_compiler.requires_env_vars_setup():
        host_compiler.setup_env_vars()

    for target in host_compiler_targets.targets:
        _setup_host_compiler_target_build_dir(host_compiler=host_compiler, target_build_dir=target)

    if host_compiler.requires_env_vars_setup():
        host_compiler.teardown_env_vars()


def _setup_host_compiler_target_build_dir(host_compiler: build_system.compiler.installed_instance.CompilerInstance,
                                          target_build_dir: build_system.build_target.build_target_cls.BuildTarget):
    # TODO
    ...
