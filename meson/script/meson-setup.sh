#!/usr/bin/env bash

# See: https://gist.github.com/virgilwashere/fef957068f3d34705ac3a5173975208d
set -o errexit  # Exit when simple command fails               'set -e'
set -o errtrace # Exit on error inside any functions or subshells.
set -o nounset  # Trigger error when expanding unset variables 'set -u'
set -o pipefail # Do not hide errors within pipes              'set -o pipefail'
IFS=$'\n\t'

project_root_dir="${BASH_SOURCE%/*}"
project_build_dir="${project_root_dir}/build"
project_machine_files_dir="${project_root_dir}/meson/machine"
project_native_machine_files_dir="${project_machine_files_dir}/native"

arch="$(uname -m)"
if [ "${arch}" == 'x86_64' ]; then
    arch='x64'
fi

source "${project_root_dir}/meson/script/detect-os/detect-os.sh"
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