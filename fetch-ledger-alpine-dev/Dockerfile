FROM alpine:3.8

RUN mkdir /build && \
	mkdir /project && \
	apk add \
	bash \
	cmake \
	make \
	musl-dev \
	openssl-dev \
	python3-dev \
	gcc \
	g++ \
	clang-dev \
	linux-headers

ENV CC=clang
ENV CXX=clang++

WORKDIR /build