#!/bin/bash
set -e

set-docker-credentails-helpers() {
    local DOCKER_CONFIG_DIR=~/.docker
    mkdir -p "$DOCKER_CONFIG_DIR"
    echo "{
      \"credHelpers\": {
        \"gcr.io\": \"gcloud\",
        \"us.gcr.io\": \"gcloud\",
        \"eu.gcr.io\": \"gcloud\",
        \"asia.gcr.io\": \"gcloud\",
        \"staging-k8s.gcr.io\": \"gcloud\"
      }
    }" >> "$DOCKER_CONFIG_DIR"/config.json
}

set-docker-credentails-helpers
./scripts/docker-publish-img.sh
./scripts/docker-delete-img-from-cache.sh

