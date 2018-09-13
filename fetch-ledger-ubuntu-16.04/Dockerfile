FROM ubuntu:16.04

USER root

RUN apt-get update && \
    apt-get install -y dialog && \
    apt-get install -y apt-utils && \
    apt-get upgrade -y && \
    apt-get install -y gcc && \
    apt-get install -y g++ && \
    apt-get install -y gdb && \
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

RUN apt-get install -y emacs24 && \
    apt-get install -y make && \
    apt-get install -y cmake && \
    apt-get install -y git && \
    apt-get install -y libssl-dev && \
    apt-get install -y python-pip && \
    python -m pip install --upgrade pip && \
    python -m pip install --upgrade cldoc && \
    ( \
        unset CC && \
        unset CXX && \
        python -m pip install jupyter \
    )
RUN apt-get install -y libboost-all-dev && \
    apt-get install -y less && \
    apt-get install -y curl && \
    apt-get install -y wget && \
    apt-get install -y gource && \
    apt-get install -y phantomjs && \
    apt-get install -y libpng-dev && \
    apt-get install -y zlib1g-dev

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib:/usr/lib

USER default

COPY home/* /home/default/

WORKDIR /build
ENTRYPOINT []

