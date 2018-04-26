#!/bin/bash
set -e
MY_DIR=${0%/*}
echo MY_DIR="$MY_DIR"
"$MY_DIR"/scripts/docker-build-img.sh
"$MY_DIR"/scripts/docker-run.sh echo something
"$MY_DIR"/scripts/docker-make.sh --help

