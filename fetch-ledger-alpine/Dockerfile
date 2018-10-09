FROM alpine:3.8

RUN mkdir /build && \
	apk add \
		bash \
		cmake \
		make \
		musl-dev \
		openssl-dev \
		python3-dev \
		gcc \
		git \
		g++ \
		clang-dev \
		libexecinfo-dev \
		linux-headers

ENV CC=clang
ENV CXX=clang++

WORKDIR /build
