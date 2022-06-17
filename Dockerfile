FROM python:3.10.5-slim-bullseye

RUN apt update && apt install --yes \
    curl \
    iproute2 \
    tcpdump

WORKDIR /home

COPY urllib3/ urllib3/
RUN pip install -e ./urllib3

RUN pip install requests

# 'docker exec -it <container-name> bash' in then run script manually
ENTRYPOINT [ "sleep", "infinity" ]


# tc qdisc add dev eth0 root tbf rate 10mbit latency 50ms burst 1540