# docker-images
Dockerfiles, scripts and setup necesary to build & use docker images used by Fetch.ai (e.g. for build, CI, etc. ...)

This repository offers set of general bash scripts located in the `scripts` folder, which are designed to be used to build & use any docker image.

# Concept

1. Each docker image setup **MUST** have its own dedicated directory. Lets assume, for ilustrational purposes of this guide that directory name will be the `my_image`.

2. This dedicated directory (`my_image`) **MUST** contain following things at minumum (and can contain anything else):
   * **`scripts`** directory
      - this directory can be provided either by **symlink** pointing to git repo `scripts` dir (which is suggested way), or by copy (discouraged).
   * **`docker-env.sh`** file
      - this file defines set of environment variables which define docker image setup for building & usage.
      - scripts from `scripts` direcory need this file to be present at this location (parent folder of `scripts` folder) since they are using enviroment variables defined by this file for they operations.

3. Scripts can be executed from anywhere (any directory on host OS filesystem).

   However, be aware that `docker-run.sh` and `docker-make.sh` scripts mount **current working directory** from host OS filesystem as volume in to the docker running container, making it available (read & write) in the running container.
   
# The `docker-env.sh` file
This file defines the docker image setup for building, deployment and running.

It allows to set small set of environment variables which are used by scripts, where only one env var is mandatory to be set really.

The `scripts/docker-env.template.sh` file is template which is supposed to be used by copy to create new `docker-env.sh` file in to its own dedicated directory. Please refer to this file to get list of variables and detailed description.

# Example how to create new image & use scripts with it

> Creating new image
```bash
git clone https://github.com/uvue-git/docker-images.git
cd docker-images
mkdir my_image
cd my_image
ln -s ../scripts scripts

## EITHER copy temaple file and edit it manually:
#cp ../scripts/docker-env.template.sh docker-env.sh
## (then edit it manually by setting DOCKER_IMAGE_TAG=my_image:latest)
## OR execute following line:
echo "DOCKER_IMAGE_TAG=my_image:latest" > docker-env.sh

# Create trivial dockerfile:
cat "FROM centos/devtoolset-4-toolchain-centos7:latest" > Dockerfile

# Commit to git if desired:
#git add .
#git commit -m "Addin my_image"
```

> Building new image:
```bash
cd docker-images
my_image/scripts/docker-build-img.sh
```

> Publishing (pushing) newly created image to docker registry:
```bash
cd docker-images
my_image/scripts/docker-publish-img.sh
```

> Pulling image from docker registry = no necessity to build it locally (the first step above) if it was already published in to external docker registry:
```bash
cd docker-images
my_image/scripts/docker-pull-img.sh
```

> Starting executable in docker container. We start `bash` shell in this example, which is very convenient since it remains running and user can interactively execute commands in running docker container from there:
```bash
cd docker-images
my_image/scripts/docker-run.sh bash
```

> Direct execution of build (the `make` in this specific example, but it can be changed in the `docker-env.sh` file). This is just convenience command - it spins up container, executes build process in there, and exits the container.
```bash
cd docker-images
my_image/scripts/docker-make.sh --help
```

# Advanced examples of scripts usage
Some scripts allow to provide parameters for docker and additional stuff. Please refer to specific scripts to get details if they support additional parameters, if they do they contain comment section at the top of the script with usage & examples.

NOTE: PLease note that the **standalone** `--` parameter (with whitespace characters around it from **both** sides) separates parameters to two groups: parameters listed to the left of it will form the "left" group and will be send to `docker` command (meaning they need to conform to parameters defined by `docker` command line manual), and the parameters listed to the right of it will form the "right" group and will be provided for the purpose whcih contextually matches the script meaning - please see examples bellow for detailed explanation.

> Advanced usage of the `docker-build-img.sh`
```bash
cd docker-images

my_image/scripts/docker-build-img.sh --squash --cpus 4 --compress --

# Above commandline example recognise the `--squash --cpus 4 --compress` parameters as
# the `right` group (to the right of the standalone `--` parameter) and will be sent 
# to the `docker build` command as IMMEDIATE_PARAMS (see bellow). The `right` group of
# parameters will be empty (as there are no paremeters provided to the right of the
# standalone `--` parameter) and will be set to the TAIL_PARAMS (= empty value), see
# bellow.
# Where general definition of the low level docker build commandline is:
#   docker build $IMMEDIATE_PARAMS -t $DOCKER_IMAGE_TAG $TAIL_PARAMS $DOCKER_BUILD_CONTEXT_DIR
# ==> And so the the resulting docker commandline (after substitution) will be:
#   docker build --squash --cpus 4 --compress -t $DOCKER_IMAGE_TAG $DOCKER_BUILD_CONTEXT_DIR
#, where DOCKER_IMAGE_TAG and DOCKER_BUILD_CONTEXT_DIR variables will be provided by 
# scripts infrastructure (by `docker-env.sh` and `docker-env-common.sh`).
```

> Advanced usage of the `docker-run.sh`
```bash
cd docker-images

my_image/scripts/docker-run.sh -p 8080:80 --cpus 4 -d -- build/examples/http_server -p 80

# Above commandline example provides the `-p 8080:80 --cpus 4 -d` parameters to `docker run`
# command as DOCKER_PARAMS, and the `build/examples/http_server -p 80` as the EXECUTABLE_PARAMS,
# where low level docker run commandline is:
#   docker run -i $USE_TTY -w $WORKDIR --rm $DOCKER_PARAMS -v $(pwd):$WORKDIR $DOCKER_IMAGE_TAG $EXECUTABLE_PARAMS
# ==> And so the the resulting docker process commandline will be:
#   docker run -i $USE_TTY -w $WORKDIR --rm -p 8080:80 --cpus 4 -d -t $DOCKER_IMAGE_TAG build/examples/http_server -p 80
#, where values for USE_TTY, WORKDIR and DOCKER_IMAGE_TAG variables will be provided by
# scripts infrastructure (by `docker-env.sh` and `docker-env-common.sh`)
#
# NOTE: The `-p 8080:80` parameter exposes internal docker container network port 80
# to host OS network port 8080, what makes it externally accessible from host OS where
# docker container is running. And `-d` param will ensure that docker runtime will
# start the `build/examples/http_server` process in daemon mode (docker cli won't exit
# until at least one daemon processes is running).
```

