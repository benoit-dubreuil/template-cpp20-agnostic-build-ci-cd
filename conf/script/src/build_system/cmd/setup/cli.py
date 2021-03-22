import argparse

import build_system.cmd.hierarchy.find_build_dir
import utils.error.cls_def
import utils.error.managed


def setup():
    arg_parser = argparse.ArgumentParser(
        description=f"Creates the {build_system.cmd.hierarchy.find_build_dir.BUILD_DIR_NAME} folder and setup specific build system builds inside.")
    # TODO

    try:
        build_system.cmd.setup.setup_build_system()

    except utils.error.managed.ManagedErrorMixin as raised_error:
        raised_error.raise_or_exit_cli(arg_parser)

    except OSError as raised_error:
        unsupported_error = utils.error.cls_def.UnsupportedError(raised_error)
        unsupported_error.raise_or_exit_cli(arg_parser)
