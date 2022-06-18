# Image for the urllib3 client

FROM python:3.10.5-slim-bullseye

RUN apt update && apt install --yes \
    curl \
    iproute2 \
    tcpdump

COPY entrypoint.sh /usr/bin/

WORKDIR /home

ENTRYPOINT [ "/usr/bin/entrypoint.sh" ]
