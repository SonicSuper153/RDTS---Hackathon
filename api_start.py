import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

auth_url = "https://api-ap-south-mum-1.openstack.acecloudhosting.com:5000/v3/auth/tokens"

headers = {
    "Content-Type": "application/json"
}

# Authentication payload
data = {
    "auth": {
        "identity": {
            "methods": ["password"],
            "password": {
                "user": {
                    "name": os.getenv("AUTH_ID"),
                    "domain": {"name": "default"},
                    "password": os.getenv("AUTH_PASSWORD")
                }
            }
        }
    }
}

# Request token from Keystone
response = requests.post(auth_url, json=data, headers=headers)

if response.status_code == 201:
    token = response.headers['X-Subject-Token']
    print("✅ Authentication successful.\n")
    print("🔑 Token:", token)

    # Parse service catalog
    token_data = response.json()
    catalog = token_data['token']['catalog']
    project_id = token_data['token']['project']['id']
    print(f"Project ID: {project_id}\n")

    keystone_url = None

    print("🔍 Public service endpoints:\n")
    for service in catalog:
        service_name = service['name']
        service_type = service['type']
        for endpoint in service['endpoints']:
            if endpoint['interface'] == 'public':
                print(f"Service: {service_name} ({service_type})")
                print(f"  - URL: {endpoint['url']}\n")
                if service_type == 'identity':
                    keystone_url = endpoint['url']

    if keystone_url:
        print(f"🔑 Keystone (Identity) Public URL: {keystone_url}")
    else:
        print("⚠️ Keystone (identity) service not found in catalog.")
else:
    print("❌ Authentication failed")
    print("Status code:", response.status_code)
    print("Response:", response.text)


nova_url = None

for service in catalog:
    if service['type'] == 'compute':
        for endpoint in service['endpoints']:
            if endpoint['interface'] == 'public':
                nova_url = endpoint['url']
                break
        if nova_url:
            break

if nova_url:
    print(f"✅ Nova (Compute) URL: {nova_url}")
else:
    print("❌ Nova (compute) public URL not found in catalog.")