#!/bin/false "This script should be sourced in a shell, not executed directly"
# Code reference : https://unix.stackexchange.com/a/424498
# shellcheck disable=SC2096

# Don't export
# shellcheck disable=SC2034

readonly meson_name="meson"
readonly meson_filename_build="${meson_name}.build"