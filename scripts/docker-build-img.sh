#!/bin/bash
set -e

SCRIPTS_DIR=${0%/*}
. "$SCRIPTS_DIR"/docker-env-common.sh

docker_build_callback() {
    local IMMEDIATE_PARAMS="$1"
    local TAIL_PARAMS="$2"

    if [ -n "${DOCKERFILE}" ]; then
        TAIL_PARAMS="-f $DOCKERFILE $TAIL_PARAMS"
    fi

    local COMMAND="docker build $IMMEDIATE_PARAMS -t $DOCKER_IMAGE_TAG $TAIL_PARAMS $DOCKER_BUILD_CONTEXT_DIR"

    echo $COMMAND
    $COMMAND
}

split_params docker_build_callback "$@"

