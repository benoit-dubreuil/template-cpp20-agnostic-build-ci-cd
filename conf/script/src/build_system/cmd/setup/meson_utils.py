import contextlib
from pathlib import Path
from typing import Final

import mesonbuild.mesonmain

import build_system.build_target.build_target
import build_system.compiler.installed_instance
import utils.cli.hidden_prints
from build_system.cmd.setup.cli_print_target_info import print_target_info
from build_system.cmd.setup.find_meson_machine_file import _find_build_type_machine_file, _find_compiler_machine_file, _find_native_machine_files_dir, _find_sanitizer_machine_file


def setup_target(root_dir: Path,
                 compiler_instance: build_system.compiler.installed_instance.CompilerInstance,
                 build_target: build_system.build_target.build_target.BuildTarget,
                 compiler_env_vars_manager: contextlib.AbstractContextManager,
                 cli_mode: bool):
    meson_cli_args = _generate_meson_setup_cli_args(root_dir=root_dir,
                                                    compiler_instance=compiler_instance,
                                                    build_target=build_target)

    if cli_mode:
        print_target_info(compiler_instance=compiler_instance,
                          target_build_dir=build_target,
                          compiler_env_vars_manager=compiler_env_vars_manager)

    _run_meson(cli_mode, meson_cli_args)


def _generate_meson_setup_cli_args(root_dir: Path,
                                   compiler_instance: build_system.compiler.installed_instance.CompilerInstance,
                                   build_target: build_system.build_target.build_target.BuildTarget):
    cli_kwarg_assignment_op: Final[str] = r'='

    cli_arg_setup_cmd = r'setup'

    setup_cli_fatal_warnings = r'--fatal-meson-warnings'

    setup_cli_arg_build_type = r'--buildtype' + cli_kwarg_assignment_op + build_target.target_build_type.value
    setup_cli_arg_build_dir = str(build_target.dir)
    setup_cli_arg_source_dir = str(root_dir)

    meson_cli_args: list[str] = [cli_arg_setup_cmd,
                                 setup_cli_fatal_warnings,
                                 setup_cli_arg_build_type,
                                 *(_generate_meson_machine_files_cli_args(compiler_instance=compiler_instance, build_target=build_target)),
                                 setup_cli_arg_build_dir,
                                 setup_cli_arg_source_dir]

    return meson_cli_args


def _generate_meson_machine_files_cli_args(compiler_instance: build_system.compiler.installed_instance.CompilerInstance,
                                           build_target: build_system.build_target.build_target.BuildTarget) -> list[str]:
    import build_system.cmd.hierarchy.find_conf_dir

    meson_machine_files_dir = build_system.cmd.hierarchy.find_conf_dir.find_meson_machine_files_dir()
    native_machine_files_dir = _find_native_machine_files_dir(meson_machine_files_dir=meson_machine_files_dir)

    machine_files = _assemble_machine_files(compiler_instance=compiler_instance,
                                            build_target=build_target,
                                            meson_machine_files_dir=meson_machine_files_dir,
                                            native_machine_files_dir=native_machine_files_dir)

    machine_files_cli_args: list[str] = _machine_files_to_cli_args(machine_files=machine_files)
    _insert_setup_cli_arg_native_file(machine_files_cli_args=machine_files_cli_args)

    return machine_files_cli_args


def _assemble_machine_files(compiler_instance: build_system.compiler.installed_instance.CompilerInstance,
                            build_target: build_system.build_target.build_target.BuildTarget,
                            meson_machine_files_dir: Path,
                            native_machine_files_dir: Path) -> list[Path]:
    return [meson_machine_files_dir / r'pre-global',
            native_machine_files_dir / r'native',
            _find_compiler_machine_file(native_machine_files_dir=native_machine_files_dir, compiler_instance=compiler_instance),
            _find_build_type_machine_file(native_machine_files_dir=native_machine_files_dir, build_target=build_target),
            _find_sanitizer_machine_file(native_machine_files_dir=native_machine_files_dir, build_target=build_target),
            meson_machine_files_dir / r'post-global']


def _machine_files_to_cli_args(machine_files: list[Path]) -> list[str]:
    return [str(machine_file) for machine_file in machine_files]


def _insert_setup_cli_arg_native_file(machine_files_cli_args: list[str]) -> None:
    setup_cli_arg_native_file: Final[str] = r'--native-file'
    step: Final[int] = 2

    for i in range(0, len(machine_files_cli_args) * step, step):
        machine_files_cli_args.insert(i, setup_cli_arg_native_file)


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
