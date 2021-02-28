#!/usr/bin/env bash

source "lib/shell-header.sh"
source "lib/get-script-dir.sh"

find_project_root_dir() {
    echo
}

readonly project_root_dir="$(get_script_dir)"
readonly project_build_dir="${project_root_dir}/build"
readonly project_machine_files_dir="${project_root_dir}/meson/machine"
readonly project_native_machine_files_dir="${project_machine_files_dir}/native"

arch="$(uname -m)"
if [ "${arch}" == 'x86_64' ]; then
    arch='x64'
fi

# Add script for vars for this
source "${project_root_dir}/script/lib/detect-os/detect-os.sh"
os="$(os_name)"

# $1 : Compiler. Ex : 'msvc'.
# $2 : Build type. Ex : 'debug'.
setup_build_dir() {
    local compiler="${1}"
    local build_type="${2}"

    local build_dir="${project_build_dir}/${os}-${arch}-${compiler}-${build_type}"

    local setup_native_files_args="--native-file ${project_machine_files_dir}/pre-global.ini"
    setup_native_files_args+=" --native-file ${project_native_machine_files_dir}/native.ini"
    setup_native_files_args+=" --native-file ${project_native_machine_files_dir}/compiler/${compiler}.ini"
    setup_native_files_args+=" --native-file ${project_native_machine_files_dir}/build_type/${build_type}.ini"
    setup_native_files_args+=" --native-file ${project_machine_files_dir}/post-global.ini"

    rm -r "${build_dir}"
    mkdir -p "${build_dir}"

    # Voluntary word splitting
    # shellcheck disable=SC2086
    meson setup "${build_dir}" "${project_root_dir}" ${setup_native_files_args}
}

setup_build_dir 'msvc' 'debug'
