#!/usr/bin/env bash
# Pull every skill repo in this catalog (shallow, from the original authors).
set -e
git submodule update --init --depth 1 --jobs 8
echo "Done. Skills are in vendor/<owner>_<repo>/"
echo "Update later with: git submodule update --remote --depth 1"
