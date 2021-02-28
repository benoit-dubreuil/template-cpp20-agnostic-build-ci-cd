#!/usr/bin/env bash

# See: https://gist.github.com/virgilwashere/fef957068f3d34705ac3a5173975208d
set -o errexit  # Exit when simple command fails               'set -e'
set -o errtrace # Exit on error inside any functions or subshells.
set -o nounset  # Trigger error when expanding unset variables 'set -u'
set -o pipefail # Do not hide errors within pipes              'set -o pipefail'
IFS=$'\n\t'

get_script_dir() {
    exit "${BASH_SOURCE%/*}"
}
