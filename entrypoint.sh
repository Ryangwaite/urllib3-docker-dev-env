#!/bin/sh

# Entrypoint script for the urllib3-client image

# Limit egress connection speed to 10mbps
# NOTE: Needs the NET_ADMIN capability
tc qdisc add dev eth0 root tbf rate 10mbit latency 50ms burst 1540

URLLIB3=/home/urllib3
if [ ! -d "$URLLIB3" ]; then
    echo "Couldn't find urllib3. Remember to mount it into the container"
    exit 1
fi

pip install -e "$URLLIB3"

# Don't exit - docker exec ... in and run commands
sleep infinity
