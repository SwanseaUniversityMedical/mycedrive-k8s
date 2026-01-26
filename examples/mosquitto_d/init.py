import os
import time
import json
import requests
from os import path
from requests.exceptions import HTTPError, RequestException, Timeout


def build_registry_url() -> str:
    # Prefer explicit override
    env_url = os.getenv("REGISTRY_URL")
    if env_url:
        return env_url

    # Fall back to in-cluster service env vars injected by Kubernetes
    host = os.getenv("MYCEDRIVE_SERVICE_HOST")
    port = os.getenv("MYCEDRIVE_SERVICE_PORT", "3333")
    if host:
        return f"http://{host}:{port}/register"

    # Last resort: rely on cluster DNS
    return "http://mycedrive:3333/register"


url = build_registry_url()

data = dict(os.environ)
print(data)

response = None
try:
    response = requests.post(url, json=data, timeout=5)
    response.raise_for_status()
except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except (Timeout, RequestException) as err:
    print(f"Request failed: {err}")
except Exception as err:
    print(f"Other error occurred: {err}")
else:
    print("Success!")

print(response)
sec = 0

while not path.exists('/dmtcp/bin/dmtcp_launch'):
    time.sleep(1)
    sec += 1


print(f'ready: {sec}')
