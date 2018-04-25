#!/bin/bash

cd ${0%/*}
. ./docker-env-common.sh

FULL_IMAGE_TAG="$DOCKER_CONTAINER_REGISTRY"/"$DOCKER_IMAGE_TAG"
docker rmi "$DOCKER_IMAGE_TAG"
docker rmi "$FULL_IMAGE_TAG"
docker rmi $(docker images -f dangling=true -q)

