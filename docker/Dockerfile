FROM ubuntu:24.04

RUN mkdir /app

COPY ./ /app

WORKDIR /app

RUN chmod +x docker/start.sh

RUN apt update -y

RUN apt install python3.12 python3.12-venv python3-dev build-essential -y

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "/app/docker/start.sh"]