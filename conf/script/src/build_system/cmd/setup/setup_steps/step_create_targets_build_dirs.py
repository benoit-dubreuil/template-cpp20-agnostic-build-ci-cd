from pathlib import Path

import build_system.build_target.compiler_instance_targets
import build_system.compiler.installed_instance


def create_targets_build_dirs(root_dir: Path,
                              host_compilers: list[build_system.compiler.installed_instance.CompilerInstance]) \
        -> list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]:
    from build_system.cmd.setup.create_targets_dirs import create_host_compilers_targets_build_dirs

    host_compilers_targets = create_host_compilers_targets_build_dirs(root_dir=root_dir,
                                                                      supported_installed_compilers=host_compilers)

    return host_compilers_targets
