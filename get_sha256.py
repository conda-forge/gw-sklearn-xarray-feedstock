# %%
import requests
import hashlib


def get_sha256_hash(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    sha256_hash = hashlib.sha256(response.content).hexdigest()
    return sha256_hash


url = "https://github.com/mmann1123/sklearn-xarray/archive/refs/tags/0.5.1_gw.tar.gz"
hash_value = get_sha256_hash(url)
print(f"SHA-256 hash: {hash_value}")

# %%
