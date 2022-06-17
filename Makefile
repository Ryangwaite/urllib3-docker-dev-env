
SECRETS ?= secrets
SERVER_KEY = "${SECRETS}/server-key.pem"
SERVER_CRT = "${SECRETS}/server-crt.pem"


# Create the self-signed cert and priv-key for the upload server
# so the client can establish SSL connection to it.
.PHONY: pki
pki:
	@echo "Creating pki..."
	@# Create certificate and key
	@mkdir -p "${SECRETS}"
	@openssl req -x509 \
		-newkey rsa:4096 \
		-keyout "${SERVER_KEY}" \
		-out "${SERVER_CRT}" \
		-sha256 \
		-nodes \
		-days 365;


# Create the files to upload
.PHONY: files
files:
	@dd if=/dev/zero of=data-for-upload/500MB.bin bs=1 count=0 seek=500M


all: pki files