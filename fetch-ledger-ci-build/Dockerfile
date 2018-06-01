FROM gcr.io/organic-storm-201412/fetch-ledger-develop:latest

COPY . /build
RUN cd /build && \
    sudo -E ci-image/cmake-make.sh

