import requests

class NetworkCreator:
    def __init__(self, token, network_name = "blue-net"):
        self.token = token
        self.network_name = network_name
        self.url = "https://api-ap-south-mum-1.openstack.acecloudhosting.com:9696/v2.0/networks"
        self.header = {
            "Content-Type": "application/json",
            "X-Auth-Token": self.token
        }

        self.payload = {
        "network": {
            "name": network_name,
            "admin_state_up": True
        }
    }

    def create_network(self):
        
        response = requests.post(self.url, headers=self.header, json=self.payload)

        if response.status_code == 201:
            net = response.json()["network"]
            print(f"Network '{net['name']}' created with ID: {net['id']}")
            return net["id"]
        else:
            print("Error creating network:", response.status_code, response.text)
