#!/usr/bin/env bash

source "lib/shell-header.sh"
source "lib/get-script-dir.sh"

project_root_dir="$(get_script_dir)"

echo -n 'Project root directory : '
echo "${project_root_dir}"