import argparse
import sys

import utils.error.meta
import utils.error.status


class ExitCLIErrorMixin(metaclass=utils.error.meta.ErrorMeta):

    def exit_cli(self, arg_parser: argparse.ArgumentParser, print_usage: bool = False) -> None:
        assert isinstance(self, utils.error.status.EncodedError)

        if print_usage:
            arg_parser.print_usage(sys.stderr)

        arg_parser.exit(self.get_error_status(), str(self))
