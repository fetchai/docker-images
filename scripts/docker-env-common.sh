DOCKER_IMAGE_TAG=
DOCKER_CONTAINER_REGISTRY=gcr.io/organic-storm-201412
WORKDIR=/build

DOCKER_ENV_SCRIPT=docker-env.sh
DOCKER_ENV_SCRIPT_PATH="$(dirname "$(pwd)")"/"$DOCKER_ENV_SCRIPT"

if [ -f "$DOCKER_ENV_SCRIPT_PATH" ]; then
    . "$DOCKER_ENV_SCRIPT_PATH"
else
    echo "WARNING: The '$DOCKER_ENV_SCRIPT_PATH' file does not exists."
fi

echo ["$DOCKER_ENV_SCRIPT"] DOCKER_IMAGE_TAG="${DOCKER_IMAGE_TAG:?"It is neccessary to set the DOCKER_IMAGE_TAG env var in the '$DOCKER_ENV_SCRIPT_PATH' file and it must be set to non-empty value"}"
echo ["$DOCKER_ENV_SCRIPT"] DOCKER_CONTAINER_REGISTRY="${DOCKER_CONTAINER_REGISTRY:?"It is neccessary to set the DOCKER_CONTAINER_REGISTRY env var either in '"$0"' or in the '$DOCKER_ENV_SCRIPT_PATH' file, and it must be set to non-empty value"}"

REGISTRY_DOCKER_IMAGE_TAG="$DOCKER_CONTAINER_REGISTRY"/"$DOCKER_IMAGE_TAG"

