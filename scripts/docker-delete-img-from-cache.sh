#!/bin/sh -ex 

SCRIPTS_DIR=${0%/*}
. "$SCRIPTS_DIR"/docker-env-common.sh

delete_dangling_layers() {
    local LAYERS=$(docker images -f dangling=true -q)
    if [ -n "$LAYERS" ]
    then 
        docker rmi $LAYERS
    fi
}
delete_image "$DOCKER_IMAGE_TAG"
delete_image "$REGISTRY_DOCKER_IMAGE_TAG"
delete_dangling_layers

