from pathlib import Path
from typing import Final

import build_system.build_target.compiler_instance_targets
import build_system.compiler.installed_instance


def setup_targets(root_dir: Path,
                  targets: list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets],
                  cli_mode: bool):
    for compiler_instance_targets in targets:
        _setup_compiler_instance_targets(root_dir=root_dir, compiler_instance_targets=compiler_instance_targets, cli_mode=cli_mode)


def _setup_compiler_instance_targets(root_dir: Path,
                                     compiler_instance_targets: build_system.build_target.compiler_instance_targets.CompilerInstanceTargets,
                                     cli_mode: bool):
    from build_system.cmd.setup.meson_utils import setup_target

    compiler_instance: Final[build_system.compiler.installed_instance.CompilerInstance] = compiler_instance_targets.compiler_instance

    with compiler_instance.create_env_vars_context_manager() as compiler_env_vars_manager:
        for target in compiler_instance_targets.build_targets:
            setup_target(root_dir=root_dir,
                         host_compiler=compiler_instance,
                         compiler_env_vars_manager=compiler_env_vars_manager,
                         target_build_dir=target,
                         cli_mode=cli_mode)
