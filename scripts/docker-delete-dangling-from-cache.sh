#!/bin/bash -e

delete_dangling_layers() {
    local LAYERS=$(docker images -f dangling=true -q)
    if [[ -n ${LAYERS} ]]
    then 
        echo "rmi -f $LAYERS"
	docker rmi -f $LAYERS
    fi
}

delete_dangling_layers

