#!/bin/false "This script should be sourced in a shell, not executed directly"
# Code reference : https://unix.stackexchange.com/a/424498
# shellcheck disable=SC2096

get_script_dir() {
    echo "${BASH_SOURCE%/*}"
}
