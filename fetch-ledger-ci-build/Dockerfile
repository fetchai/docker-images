FROM gcr.io/organic-storm-201412/fetch-ledger-develop:latest

COPY . /build
RUN cd /build && \
    ls -al && \
    sudo ci-image/cmake-make.sh

