FROM alpine:3.8

RUN mkdir -p /app/data && \
	apk add \
	openssl \
	libstdc++ \
	python3 \
	libgcc

ADD requirements.txt /app

RUN pip3 install -r /app/requirements.txt

WORKDIR /app/data
ADD constellation /app
ADD monitor.py /app

EXPOSE 8000-8020

ENTRYPOINT ["/app/monitor.py"]

