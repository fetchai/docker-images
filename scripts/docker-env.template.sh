#!/nin/bash

#############################################################################
### **MANDATORY** variables section
# Variables in this section **MUST** be set in `docker-env.sh` file

# ---------------------------------------------------------------------------
# This variable defines docker image tag (*WIHOUT* container registry URI prefix).
# Example: DOCKER_IMAGE_TAG=fetch-ledger-develp:latest
DOCKER_IMAGE_TAG=


#############################################################################
### **NON**-mandatory variables
# They **can** be overriden in this file. Their default value is defined by scripts insfrastructure.

# ---------------------------------------------------------------------------
# This variable defines URI of docker image **registry** where newly created
# images will be pushed in to, or pulled from (by `docker-publish-img.sh` and
# `docker-pull-img.sh` scripts).
# It defaults to `docker-publish-img.sh`.
#DOCKER_CONTAINER_REGISTRY=

# ---------------------------------------------------------------------------
# This variable defines the context directory for docker build (`docker-build-img.sh` 
# script).
# This means that docker build process will have access exclusivelly to this 
# directory on from **host OS** during build process (COPY and ADD instructions
# in dockerfile). Host OS filesystem beyond this directory (= parent folders)
# will **NOT** be accessible during docker build process.
# It defaults to the **very same** directory where `docker-env.sh` file is located.
#DOCKER_BUILD_CONTEXT_DIR=


# ---------------------------------------------------------------------------
# This variable Defines path to custom dockerfile.
# It defaults to the `Dockerfile` file located in the **very same** directory
# where the `docker-env.sh` file is located.
#DOCKERFILE=

# ---------------------------------------------------------------------------
# This variable defines path to executable/script which executes build (usually make)
# This variable is used exclusivelly by the `scriots/docker-make.sh` script,
# so it does **not** affect other scripts)
# It must be etiher absolute path, or relative to the working directory 'WORKDIR' in the running docker container environment!
# It defaults to the `scripts/docker-local-make.sh` script.
#DOCKER_LOCAL_MAKE=

# ---------------------------------------------------------------------------
# This variable defines directory in the running docker container (**not** on host OS),
# in to which a volume will be mounted by `docker-run.sh` script.
# The volume is defined by current working directory on **host OS** where
# the `docker-run.sh` script is excuted.
# Defaults to `/docker`.
#WORKDIR=


