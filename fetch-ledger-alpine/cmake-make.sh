#!/bin/bash
CMAKE_BUILD_DIR=build-alpine

mkdir -p "$CMAKE_BUILD_DIR"
cd "$CMAKE_BUILD_DIR"

cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DFETCH_DISABLE_COLOUR_LOG=TRUE ..
make -j "$@"

