import utils.cli
from build_system.cmd.hierarchy.find_root_dir import find_root_dir
from build_system.cmd.hierarchy.find_root_dir import cli

if __name__ == '__main__':
    utils.cli.init()

    root = find_root_dir(cli.get_error_formatted_msg_root_not_found)
    print(root, end=str())

    utils.cli.deinit()
