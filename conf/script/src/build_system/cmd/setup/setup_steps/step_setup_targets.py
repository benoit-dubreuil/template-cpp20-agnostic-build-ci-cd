from pathlib import Path
from typing import Final

import build_system.build_target.compiler_instance_targets
import build_system.compiler.installed_instance


def setup_targets(root_dir: Path,
                  host_compilers_targets: list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets],
                  cli_mode: bool):
    for host_compiler_targets in host_compilers_targets:
        _setup_host_compiler_targets(root_dir=root_dir, host_compiler_targets=host_compiler_targets, cli_mode=cli_mode)


def _setup_host_compiler_targets(root_dir: Path,
                                 host_compiler_targets: build_system.build_target.compiler_instance_targets.CompilerInstanceTargets,
                                 cli_mode: bool):
    from build_system.cmd.setup.meson_utils import setup_host_compiler_target

    host_compiler: Final[build_system.compiler.installed_instance.CompilerInstance] = host_compiler_targets.compiler_instance

    with host_compiler.create_env_vars_context_manager() as compiler_env_vars_manager:
        for target in host_compiler_targets.targets:
            setup_host_compiler_target(root_dir=root_dir,
                                       host_compiler=host_compiler,
                                       compiler_env_vars_manager=compiler_env_vars_manager,
                                       target_build_dir=target,
                                       cli_mode=cli_mode)
