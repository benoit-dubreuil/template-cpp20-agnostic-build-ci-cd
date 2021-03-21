import argparse

import utils.error.cls_def
import utils.error.managed
from build_system import cmd
from build_system.cmd.hierarchy.find_build_dir.impl import BUILD_DIR_NAME


def setup():
    arg_parser = argparse.ArgumentParser(
        description=f"Creates the {BUILD_DIR_NAME} folder and setup specific build system builds inside.")
    # TODO

    try:
        cmd.setup.setup()

    except utils.error.managed.ManagedErrorMixin as raised_error:
        raised_error.raise_or_exit_cli(arg_parser)

    except OSError as raised_error:
        if not isinstance(raised_error, utils.error.managed.ManagedErrorMixin):
            unsupported_error = utils.error.cls_def.UnsupportedError(raised_error)
            unsupported_error.raise_or_exit_cli(arg_parser)
