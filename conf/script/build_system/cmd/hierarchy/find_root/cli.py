import utils.cli
from build_system.cmd.hierarchy import find_root


def get_error_formatted_msg_root_not_found() -> str:
    return utils.cli.format_error_msg(find_root.get_error_msg_root_not_found())
