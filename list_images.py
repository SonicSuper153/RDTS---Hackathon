import requests

# You should already have:
# - token (X-Subject-Token)
# - project_id (from token_data['token']['project']['id'])
# - nova_url (from service catalog, where service['type'] == 'compute')

# Example: nova_base_url = "https://nova-endpoint-url/v2.1"
# Full URL is usually <nova_base_url>/flavors

headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": "gAAAAABoFdtaQhOAQygzkCXSJMPCsNInLeJu5mrWT3oImGQGo8_uqVr0Y9Uz71UXfRBBvwuBmTgM3B33p1pBwps9Yo37wW2xnE9X_DAQ-PunquRkFSB0IWu9CdfIpt-x_Og6-aeus3O3otgFC0nveZH-MNvJKSFW1b56GhMSzAHtVahJOpTPJW4"
}

# Replace with your actual Nova base URL
nova_base_url = "https://api-us-east-at-1.openstack.acecloudhosting.com:8774/v2.1"

response = requests.get(f"{nova_base_url}/flavors/detail", headers=headers)

if response.status_code == 200:
    flavors = response.json()["flavors"]
    print("✅ Available Flavors:")
    for flavor in flavors:
        print(f"- ID: {flavor['id']}, Name: {flavor['name']}, RAM: {flavor['ram']}MB, vCPUs: {flavor['vcpus']}, Disk: {flavor['disk']}GB")
else:
    print("❌ Failed to fetch flavors")
    print("Status code:", response.status_code)
    print("Response:", response.text)
