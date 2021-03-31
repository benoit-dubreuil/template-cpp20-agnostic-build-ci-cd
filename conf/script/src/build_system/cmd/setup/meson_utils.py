import contextlib
from pathlib import Path
from typing import Final

import mesonbuild.mesonmain

import build_system.build_target.build_target_cls
import build_system.compiler.installed_instance
import utils.cli.hidden_prints
from build_system.cmd.setup.cli_print_target_info import print_target_info


def setup_host_compiler_target_build_dir(root_dir: Path,
                                         host_compiler: build_system.compiler.installed_instance.CompilerInstance,
                                         target_build_dir: build_system.build_target.build_target_cls.BuildTarget,
                                         compiler_env_vars_manager: contextlib.AbstractContextManager,
                                         cli_mode: bool):
    meson_cli_args = _generate_meson_setup_cli_args(root_dir=root_dir,
                                                    host_compiler=host_compiler,
                                                    target_build_dir=target_build_dir)

    if cli_mode:
        print_target_info(host_compiler=host_compiler,
                          target_build_dir=target_build_dir,
                          compiler_env_vars_manager=compiler_env_vars_manager)

    _run_meson(cli_mode, meson_cli_args)


def _generate_meson_setup_cli_args(root_dir: Path,
                                   host_compiler: build_system.compiler.installed_instance.CompilerInstance,
                                   target_build_dir: build_system.build_target.build_target_cls.BuildTarget):
    cli_kwarg_assignment_op: Final[str] = r'='

    cli_arg_setup_cmd = r'setup'

    setup_cli_arg_build_type = r'--buildtype' + cli_kwarg_assignment_op + target_build_dir.get_build_type().value
    setup_cli_arg_build_dir = str(target_build_dir.dir)
    setup_cli_arg_source_dir = str(root_dir)

    meson_cli_args: list[str] = [cli_arg_setup_cmd,
                                 setup_cli_arg_build_type,
                                 *(_generate_meson_machine_files_cli_args(host_compiler=host_compiler, target_build_dir=target_build_dir)),
                                 setup_cli_arg_build_dir,
                                 setup_cli_arg_source_dir]

    return meson_cli_args


def _generate_meson_machine_files_cli_args(host_compiler: build_system.compiler.installed_instance.CompilerInstance,
                                           target_build_dir: build_system.build_target.build_target_cls.BuildTarget) -> list[str]:
    import build_system.cmd.hierarchy.find_conf_dir

    native_dir_name: Final[str] = r'native'
    meson_machine_files_dir: Final[Path] = build_system.cmd.hierarchy.find_conf_dir.find_meson_machine_files_dir()

    native_machine_files_dir: Path = meson_machine_files_dir / native_dir_name
    native_machine_files_dir.resolve(strict=True)
    native_machine_files_dir = native_machine_files_dir.absolute()

    all_machine_files: list[Path] = [native_machine_files_dir / r'pre-global',
                                     native_machine_files_dir / r'post-global']

    _concatenate_extension_to_machine_files(all_machine_files)
    
    all_machine_file_cli_args: list[str] = _machine_files_to_cli_args(all_machine_files=all_machine_files)
    _insert_setup_cli_arg_cross_file(all_machine_file_cli_args=all_machine_file_cli_args)

    # TODO : Concatenate before setup_cli_arg_cross_file

    return all_machine_file_cli_args


def _concatenate_extension_to_machine_files(all_machine_files: list[Path]) -> None:
    extension: Final[str] = r'.ini'

    for i in range(len(all_machine_files)):
        machine_file = all_machine_files[i]

        machine_file.with_suffix(extension)
        machine_file.resolve(strict=True)

        all_machine_files[i] = machine_file


def _machine_files_to_cli_args(all_machine_files: list[Path]) -> list[str]:
    return [str(machine_file) for machine_file in all_machine_files]


def _insert_setup_cli_arg_cross_file(all_machine_file_cli_args: list[str]) -> None:
    setup_cli_arg_cross_file: Final[str] = r'--cross-file'

    for i in range(stop=len(all_machine_file_cli_args), step=2):
        all_machine_file_cli_args.insert(i, setup_cli_arg_cross_file)


def _run_meson(cli_mode, meson_cli_args):
    meson_launcher: str = _fetch_meson_launcher()

    try:
        with contextlib.nullcontext() if cli_mode else utils.cli.hidden_prints.HiddenPrints():
            mesonbuild.mesonmain.run(meson_cli_args, meson_launcher)

    except SystemExit:
        pass


def _fetch_meson_launcher() -> str:
    current_package_path = _fetch_current_package_path()
    return str(current_package_path)


def _fetch_current_package_path() -> Path:
    current_package_path = Path(__file__).parent
    current_package_path.resolve(strict=True)
    current_package_path = current_package_path.absolute()

    return current_package_path
