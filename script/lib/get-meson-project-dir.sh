#!/bin/false "This script should be sourced in a shell, not executed directly"
# Code reference : https://unix.stackexchange.com/a/424498
# shellcheck disable=SC2096

source "vars-meson-structure.sh"
source "get-script-dir.sh"

get_meson_project_dir() {
    local meson_project_dir="$(get_script_dir)"

    while [[ ! -f "${meson_filename_build}" && "${meson_project_dir}" != '/' && "${meson_project_dir}" != '.' ]]; do
        meson_project_dir="$(dirname -z "${meson_project_dir}")"
    done

    echo "TODO"
}
