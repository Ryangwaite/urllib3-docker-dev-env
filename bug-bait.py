#!/usr/bin/env python3

import time
import urllib3

# NOTE: Uncomment to use PyOpenSSLContext backend instead of stdlib SSLContext backend
# from urllib3.contrib import pyopenssl
# pyopenssl.inject_into_urllib3()

from urllib3.util import SSLContext
print(f"SSLContext has type {SSLContext}")

TOKEN = "uploadtoken"
BASE_URL = "http://upload-server"
# BASE_URL = "https://upload-server"

http = urllib3.PoolManager(cert_reqs='CERT_NONE')

# 1. Seed the timeout on the conn to 5 seconds
r = http.request("GET", f"{BASE_URL}/files/test.txt?token={TOKEN}", timeout=5)
print(r.data)

# 2. Upload file that takes >5 seconds to complete
# 500MB file at 500mbps bandwidth uploads in ~10.5s with the following code
with open("/var/data-for-upload/500MB.bin") as fp:
    file_data = fp.read()
upload_start = time.time()
try:
    r = http.request(
        "POST",
        f"{BASE_URL}/upload?token={TOKEN}",
        fields={
            "file": ("500MB.bin", file_data),
        },
        timeout=15,
    )
finally:
    print(f"Upload request finished in {time.time() - upload_start:.3f} seconds")
