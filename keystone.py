import requests

# Your token from the authentication response
token = 'your-auth-token'

# Keystone URL for listing projects
identity_url = "https://api-ap-south-mum-1.openstack.acecloudhosting.com:5000/v3/projects"

# Headers to authenticate the request
headers = {
    "X-Auth-Token": "gAAAAABoFddp72c6FMc7Xs_KONvkhgWmHOklsjOK2qCn0IyXOESpO56EAYJVPiwvT-xAK78gU_BrPrqRK5GbQzpbZeRkwdhq8T0eDxxP4qzDi9WMRa8Hev-8MlEpYjE714y6Sb-YNWeG-aJHD29UCqcyoIt8juEJ7P3qqpXFFmvA7o0R3FCTrKE",
    "Content-Type": "application/json"
}

# Make the request to the Keystone API
response = requests.get(identity_url, headers=headers)

# Check the response status
if response.status_code == 200:
    projects = response.json()
    print("Projects List:")
    for project in projects['projects']:
        print(f"Project ID: {project['id']}, Project Name: {project['name']}")
else:
    print(f"Failed to get projects: {response.status_code}, {response.text}")