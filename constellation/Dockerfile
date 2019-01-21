FROM alpine:3.8 AS builder

RUN mkdir -p /app/build && \
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

ADD project.tar.gz /app

WORKDIR /app/build

ENV CC=clang
ENV CXX=clang++

RUN cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DFETCH_DISABLE_COLOUR_LOG=TRUE /app/project \
	&& make -j 7 constellation

FROM alpine:3.8


RUN mkdir -p /app/data && \
	apk add \
	openssl \
	libstdc++ \
	python3 \
	libgcc

ADD requirements.txt /app
ADD monitor.py /app

RUN pip3 install -r /app/requirements.txt

WORKDIR /app/data

COPY --from=builder /app/build/apps/constellation /app

EXPOSE 8000-8020

ENTRYPOINT ["/app/monitor.py"]

