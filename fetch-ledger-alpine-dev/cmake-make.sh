#!/bin/bash

CMAKE_BUILD_DIR=build-alpine

ls -l

mkdir -p "$CMAKE_BUILD_DIR"
cd "$CMAKE_BUILD_DIR"

cmake ..
make -j constellation

