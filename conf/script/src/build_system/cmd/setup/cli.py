import argparse

import utils.error.cls_def
import utils.error.managed
from build_system import cmd


def clean_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Creates the build folder and setup specific build system builds inside.")

    try:
        cmd.setup.setup()

    except utils.error.managed.ManagedError as raised_error:
        raised_error.raise_or_exit_cli(arg_parser)

    except OSError as raised_error:
        if not isinstance(raised_error, utils.error.managed.ManagedError):
            unsupported_error = utils.error.cls_def.UnsupportedError(raised_error)
            unsupported_error.raise_or_exit_cli(arg_parser)
