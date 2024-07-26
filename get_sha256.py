# %%
import requests
import hashlib
import yaml
from jinja2 import Template

# Step 1: Read the YAML file content
with open("./recipe/meta.yaml", "r") as file:
    yaml_content = file.read()

# Step 2: Use Jinja2 to render the template with the variables
template = Template(yaml_content)
rendered_content = template.render()

# Step 3: Parse the rendered YAML content to extract the URL
parsed_yaml = yaml.safe_load(rendered_content)
url = parsed_yaml["source"]["url"]

print(url)


def get_sha256_hash(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    sha256_hash = hashlib.sha256(response.content).hexdigest()
    return sha256_hash


# read in meta.yaml file and retrieve source URL and version


# url = "https://github.com/mmann1123/sklearn-xarray/archive/refs/tags/0.5.1_gw.tar.gz"
hash_value = get_sha256_hash(url)
print(f"SHA-256 hash: {hash_value}")

# %%
