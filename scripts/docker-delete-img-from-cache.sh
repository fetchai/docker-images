#!/bin/bash
set -e
set -x

SCRIPTS_DIR=${0%/*}
. "$SCRIPTS_DIR"/docker-env-common.sh

delete-image() {
    local IMG_TAG=$1
    docker image inspect "$IMG_TAG" >/dev/null 2>&1 && docker rmi "$IMG_TAG" || :
}

delete-dangling-layers() {
    local LAYERS=$(docker images -f dangling=true -q)
    if [[ -z ${LAYERS+x} ]]
    then 
        docker rmi $LAYERS
    fi
}
echo start
delete-image "$DOCKER_IMAGE_TAG"
echo x1
delete-image "$REGISTRY_DOCKER_IMAGE_TAG"
echo x2
delete-dangling-layers
echo stop

