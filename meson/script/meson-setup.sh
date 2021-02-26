#!/usr/bin/env bash

script_dir="${BASH_SOURCE%/*}"

meson setup "$("${script_dir}"/print-setup-dir-args.sh)"