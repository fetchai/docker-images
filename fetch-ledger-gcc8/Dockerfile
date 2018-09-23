FROM gcc:8

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       libssl-dev \
       cmake \
       cmake-curses-gui \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/bin/cmake/bin:${PATH}"

WORKDIR /build
ENTRYPOINT []

