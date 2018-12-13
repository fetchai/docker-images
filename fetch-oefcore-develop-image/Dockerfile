FROM ubuntu:18.04

USER root

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y clang && \
    apt-get install -y gcc && \
    apt-get install -y g++ && \
    apt-get install -y gdb && \
    apt-get install -y clang-tidy && \
    apt-get install -y clang-format && \
    apt-get install -y make && \
    apt-get install -y cmake && \
    apt-get install -y cmake-curses-gui && \
    apt-get install -y vim && \
    apt-get install -y llvm && \
    apt-get install -y clang-tools && \
    apt-get install -y perl-doc && \
    apt-get install -y cppcheck && \
    apt-get install -y sudo

# This adds the "default" user in to sudoers with full privileges:
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

RUN apt-get install protobuf-compiler -y && \
    apt-get install libprotobuf-dev -y

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib:/usr/lib

USER default

COPY home/* /home/default/

WORKDIR /build
ENTRYPOINT []
