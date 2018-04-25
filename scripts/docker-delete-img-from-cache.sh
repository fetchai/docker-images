#!/bin/bash

cd ${0%/*}
. ./docker-env-common.sh

delete-image() {
    local IMG_TAG=$1
    #if [[ "$(docker images -q $IMG_TAG 2> /dev/null)" == "" ]]
    #then
    #    docker rmi $IMG_TAG
    #fi
    docker image inspect "$IMG_TAG" >/dev/null 2>&1 && docker rmi "$IMG_TAG"
}

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

