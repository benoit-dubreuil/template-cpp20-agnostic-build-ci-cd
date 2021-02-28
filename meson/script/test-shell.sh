#!/usr/bin/env bash

source "shell_header.sh"
source "get_script_dir.sh"

project_root_dir="$(get_script_dir)"

echo -n 'Project root directory : '
echo "${project_root_dir}"