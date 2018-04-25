#!/bin/bash

cd ${0%/*}
. ./docker-env-common.sh
. ./docker-common.sh

docker_build_callback() {
    local DOCKER_PARAMS="$1"
    local EXECUTABLE_PARAMS="$2"
    local COMMAND="docker build $DOCKER_PARAMS -t $DOCKER_IMAGE_TAG $EXECUTABLE_PARAMS ../"
    echo $COMMAND
    $COMMAND
}

split_params docker_build_callback "$@"

