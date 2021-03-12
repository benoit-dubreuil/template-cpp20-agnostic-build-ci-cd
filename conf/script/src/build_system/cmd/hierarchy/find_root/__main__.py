from src import utils
from src.build_system.cmd import find_root
from src.build_system.cmd import cli

if __name__ == '__main__':
    utils.cli.init()
    root = find_root(cli.get_error_formatted_msg_root_not_found)
    print(root, end=str())
