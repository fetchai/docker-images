#!/bin/bash
set -e

./scripts/docker-delete-img-from-cache.sh
./scripts/docker-build-img.sh --no-cache --

