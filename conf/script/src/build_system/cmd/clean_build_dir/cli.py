import argparse


def clean_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Cleans the project's build folder, where the build system organizes into subfolders specific builds.")
