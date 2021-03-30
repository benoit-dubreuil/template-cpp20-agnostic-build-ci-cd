from pathlib import Path
from typing import Final, Optional

import build_system.build_target.compiler_instance_targets
import build_system.compiler.installed_instance
import build_system.compiler.supported_installed_instances
from build_system.cmd.setup.create_targets_dirs import create_all_host_compilers_targets_build_dirs
from build_system.cmd.setup.meson_utils import setup_host_compiler_target_build_dir


def setup_build_system(root_dir: Optional[Path] = None, cli_mode: bool = False):
    import build_system.cmd.hierarchy.assure_arg_integrity

    root_dir = build_system.cmd.hierarchy.assure_arg_integrity.assure_root_dir_exists(root_dir=root_dir)

    host_compilers = build_system.compiler.supported_installed_instances.fetch_all()
    all_host_compilers_targets = create_all_host_compilers_targets_build_dirs(root_dir=root_dir,
                                                                              supported_installed_compilers=host_compilers)

    for host_compiler_targets in all_host_compilers_targets:
        _setup_host_compiler_targets(root_dir=root_dir,
                                     host_compiler_targets=host_compiler_targets,
                                     cli_mode=cli_mode)


def _setup_host_compiler_targets(root_dir: Path,
                                 host_compiler_targets: build_system.build_target.compiler_instance_targets.CompilerInstanceTargets,
                                 cli_mode: bool):
    host_compiler: Final[build_system.compiler.installed_instance.CompilerInstance] = host_compiler_targets.compiler_instance

    if host_compiler.requires_env_vars_setup():
        host_compiler.setup_env_vars()

    for target in host_compiler_targets.targets:
        setup_host_compiler_target_build_dir(root_dir=root_dir,
                                             host_compiler=host_compiler,
                                             target_build_dir=target,
                                             cli_mode=cli_mode)

    if host_compiler.requires_env_vars_setup():
        host_compiler.teardown_env_vars()
