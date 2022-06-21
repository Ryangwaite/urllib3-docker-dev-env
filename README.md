# urllib3-test-env

## Overview

This environment was created to reproduce and fix [this](https://github.com/urllib3/urllib3/issues/2645) bug.

There's 2 docker containers:
- `upload-server` - an instance of [simple-upload-server](https://github.com/mayth/go-simple-upload-server) for sending requests to
- `urllib3-client` - urllib3 environment with slowed egress traffic for running urllib3 code

## Reproducing Bug

Requirements:
- `docker`
- `docker-compose`

1. After cloning, initialise the environment with:
```bash
make init
```
2. Start the environment with:
```bash
docker-compose up
```
3. In a new shell on the host but it in the root of the repo, run the following to exec into the `urllib3-client` container:
```bash
docker-compose exec urllib3-client bash
```
4. From the `urllib3-client` shell run the following script to trigger the bug:
```bash
python3 bug-bait.py
```
If the bug was successfully reproduced then a stacktrace containing the following error should be printed:
```bash
urllib3.exceptions.ProtocolError: ('Connection aborted.', TimeoutError('timed out'))
```

The following output will be immediately before the stack trace
```bash
Upload request finished in 5.401 seconds
```
Which is the timeout of the initial request + some overhead. If the timeout of the initial request is changed, the duration of the above output will change to track with it.

### Cleanup
Run `docker-compose down` to terminate the environment.
