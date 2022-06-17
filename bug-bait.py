#!/usr/bin/env python3

import time
import urllib3

TOKEN = "uploadtoken"

http = urllib3.PoolManager(cert_reqs='CERT_NONE')

# 1. Seed the timeout on the conn to 5 seconds
r = http.request("GET", f"https://upload-server/files/small-test.txt?token={TOKEN}", timeout=5)
print(r.data)

# 2. Upload file that takes >5 seconds to complete
# 500MB file at 500mbps bandwidth uploads in ~10.5s with the following code
with open("/var/data-for-upload/500MB.bin") as fp:
    file_data = fp.read()
upload_start = time.time()
try:
    r = http.request(
        "POST",
        f"https://upload-server/upload?token={TOKEN}",
        fields={
            "file": ("500MB.bin", file_data),
        },
        timeout=15,
    )
finally:
    print(f"Upload request finished in {time.time() - upload_start:.3f} seconds")
