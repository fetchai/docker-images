FROM ubuntu:18.04

USER root

RUN apt-get update && \
    apt-get install -y dialog && \
    apt-get install -y apt-utils && \
    apt-get upgrade -y && \
    apt-get install -y clang && \
    apt-get install -y gcc && \
    apt-get install -y g++ && \
    apt-get install -y gdb && \
    apt-get install -y clang-tidy && \
    apt-get install -y clang-format && \
    apt-get install -y cmake-curses-gui && \
    apt-get install -y llvm && \
    apt-get install -y sudo

# This adds the `default` user in to sudoers with full privileges:
RUN HOME=/home/default && \
    mkdir -p ${HOME} && \
    GROUP_ID=1000 && \
    USER_ID=1000 && \
    groupadd -r default -f -g "$GROUP_ID" && \
    useradd -u "$USER_ID" -r -g default -d "$HOME" -s /sbin/nologin \
    -c "Default Application User" default && \
    chown -R "$USER_ID:$GROUP_ID" ${HOME} && \
    usermod -a -G sudo default && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

ENV CC=/usr/bin/clang
ENV CXX=/usr/bin/clang++
ENV CCACHE_DIR=/build/docker_ccache

RUN apt-get install -y vim && \
    apt-get install -y make && \
    apt-get install -y cmake && \
    apt-get install -y git && \
    apt-get install -y python-pip && \
    python -m pip install --upgrade pip && \
    python -m pip install --upgrade cldoc && \
    ( \
        unset CC && \
        unset CXX && \
        python -m pip install jupyter \
    )

RUN apt-get install -y libboost-all-dev=1.65.1.0ubuntu1 && \
    apt-get install -y less && \
    apt-get install -y curl && \
    apt-get install -y wget && \
    apt-get install -y gource && \
    apt-get install -y phantomjs && \
    apt-get install -y libpng-dev && \
    apt-get install -y zlib1g-dev

ARG OPENSSL_VERSION_GIT_SELECTOR="OpenSSL_1_1_1b"
ENV OPENSSL_VERSION_GIT_SELECTOR="${OPENSSL_VERSION_GIT_SELECTOR}"

RUN OPENSSL_SRC_DIR="/home/default/openssl" && \
    ORIG_DIR="$(pwd)" && \
    mkdir -p "${OPENSSL_SRC_DIR}" && \
    git clone -b "${OPENSSL_VERSION_GIT_SELECTOR}" --single-branch --depth 1 https://github.com/openssl/openssl.git "${OPENSSL_SRC_DIR}" && \
    cd "${OPENSSL_SRC_DIR}" && \
    git submodule sync --recursive && \
    git submodule update --init --recursive && \
    ./config && \
    make -j && \
    make test &&\
    make install && \
    cd "${ORIG_DIR}" && \
    rm -rf "${OPENSSL_SRC_DIR}"

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib:/usr/lib

USER default

COPY home/* /home/default/

WORKDIR /build
ENTRYPOINT []

