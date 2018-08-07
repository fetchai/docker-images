FROM alpine:3.8

RUN mkdir -p /app/data && \
	apk add \
	openssl \
	libstdc++ \
	libgcc

WORKDIR /app/data
ADD constellation /app

EXPOSE 8000-8020

CMD /app/constellation -boostrap
