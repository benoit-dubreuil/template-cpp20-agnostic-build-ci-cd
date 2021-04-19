import argparse
import sys
import typing

from .status import *
from utils.meta_prog.encapsulation import *


@export
class ExitCLIErrorMixin(Exception, metaclass=ErrorMeta):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def exit_cli(self, arg_parser: argparse.ArgumentParser, print_usage: bool = False) -> typing.NoReturn:
        assert isinstance(self, EncodedErrorMixin)

        if print_usage:
            arg_parser.print_usage(sys.stderr)

        arg_parser.exit(self.get_error_status(), str(self))

    def raise_or_exit_cli(self, arg_parser: argparse.ArgumentParser, print_usage: bool = False) -> typing.NoReturn:
        if arg_parser.exit_on_error:
            self.exit_cli(arg_parser, print_usage)
        else:
            raise self
