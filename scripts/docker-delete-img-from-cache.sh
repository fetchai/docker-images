#!/bin/bash

SCRIPTS_DIR=${0%/*}
. "$SCRIPTS_DIR"/docker-env-common.sh

delete-dangling-layers() {
    local LAYERS=$(docker images -f dangling=true -q)
    if [[ -z ${LAYERS+x} ]]
    then 
        docker rmi $LAYERS
    fi
}
delete-image "$DOCKER_IMAGE_TAG"
delete-image "$REGISTRY_DOCKER_IMAGE_TAG"
delete-dangling-layers

