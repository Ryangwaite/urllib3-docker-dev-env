#!/usr/bin/env python3

import time
import requests

from urllib3.util import SSLContext
print("urllib3 is using SSLContext: ", SSLContext)

TOKEN = "uploadtoken"

s = requests.Session()

# 1. Seed the timeout on the conn to 5 seconds
response = s.get("https://upload-server/files/small-test.txt", params={"token": TOKEN}, timeout=5, verify=False)
print(response.text)

# 2. Upload file that takes >5 seconds to complete
# 500MB file at 500mbps bandwidth uploads in ~10.5s with the following code
with open("/var/data-for-upload/500MB.bin", "rb") as upload_file:
    try:
        upload_start = time.time()
        response = s.post("https://upload-server/upload", params={"token": TOKEN}, timeout=15, verify=False, files={"file":upload_file })
        print(response.text)
    finally:
        print(f"Upload request finished in {time.time() - upload_start:.3f} seconds")
