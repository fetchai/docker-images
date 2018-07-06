#!/bin/bash -e

SCRIPTS_DIR=${0%/*}

"$SCRIPTS_DIR"/docker-add_registry-cred-helpers.py
"$SCRIPTS_DIR"/docker-pull-img.sh
"$SCRIPTS_DIR"/docker-make.sh

