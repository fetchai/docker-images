#!/bin/bash -x

SCRIPTS_DIR=${0%/*}
. "$SCRIPTS_DIR"/docker-env-common.sh

delete_dangling_layers() {
    local LAYERS=$(docker images -f dangling=true -q)
    if [[ -n ${LAYERS} ]]
    then 
        echo "rmi -f $LAYERS"
	docker rmi -f $LAYERS
    fi
}

delete_dangling_layers

