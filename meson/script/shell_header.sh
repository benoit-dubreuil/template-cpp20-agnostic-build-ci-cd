#!/bin/false "This script should be sourced in a shell, not executed directly"
# Code reference : https://unix.stackexchange.com/a/424498
# shellcheck disable=SC2096

# Code reference : https://gist.github.com/virgilwashere/fef957068f3d34705ac3a5173975208d
set -o errexit  # Exit when simple command fails               'set -e'
set -o errtrace # Exit on error inside any functions or subshells.
set -o nounset  # Trigger error when expanding unset variables 'set -u'
set -o pipefail # Do not hide errors within pipes              'set -o pipefail'
IFS=$'\n\t'
