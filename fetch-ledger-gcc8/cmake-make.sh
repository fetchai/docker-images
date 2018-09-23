#!/bin/bash

CMAKE_BUILD_DIR=build-gcc8

mkdir -p "$CMAKE_BUILD_DIR"
cd "$CMAKE_BUILD_DIR"

cmake ..
make -j "$@"

