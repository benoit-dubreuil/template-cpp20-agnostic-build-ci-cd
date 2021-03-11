import utils.cli
from build_system.cmd.hierarchy.find_root import find_root
from build_system.cmd.hierarchy.find_root import cli

if __name__ == '__main__':
    utils.cli.init()
    find_root(cli.get_error_formatted_msg_root_not_found)
