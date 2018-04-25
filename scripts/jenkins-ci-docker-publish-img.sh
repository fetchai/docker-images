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
    }" >> ~/.docker/config.json
}

set-docker-credentails-helpers
./scripts/docker-deploy-img.sh
./scripts/docker-delete-img-from-cache.sh

