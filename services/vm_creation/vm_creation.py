import requests
import os
import time
from utils.file import FileHandler

class VMCreator:
    def __init__(self, token, project_id):
        self.token = token
        self.project_id = project_id
        self.header ={
            "X-Auth-Token": self.token,
            "Content-Type": "application/json"
        }
        self.url = "https://api-ap-south-mum-1.openstack.acecloudhosting.com:8774/v2.1"
        self.output_dir = "data/vm_data.json"
        self.file_handler = FileHandler()

    def create_vm(self):

        compute_url = f"https://api-ap-south-mum-1.openstack.acecloudhosting.com:8774/v2.1/a02b14bcfca64e44bd68f2d00d8555b5/servers"
        print(compute_url)
        data = {
            "server": {
                "name": "dev-box",
                "imageRef": self.image_id,
                "flavorRef": self.flavor_id,
                "block_device_mapping_v2": [
                    {
                      "boot_index": "0",
                      "uuid": self.volume_id,
                      "source_type": "volume",
                      "destination_type": "volume",
                      "delete_on_termination": True
                    }
                ],
                "networks": [  
                    {"uuid": self.network_id}
                ],
                "security_groups": [
                    {"name": "default"}
                ],
                #"key_name": self.keypair
            }
        }

        response = requests.post(compute_url, json=data, headers=self.header)

        vm_data = {
                "vm_id": response.json()["server"]["id"],
                "flavor_id": self.flavor_id,
                "image_id": self.image_id,
                "network_id": self.network_id,
                "volume_id": self.volume_id
        }

        self.file_handler.save_json(vm_data, self.output_dir)

        if response.status_code == 202:
           print("VM creation initiated successfully")

           
        else:
           print("Failed to create VM", response.status_code, response.text)

    def get_flavors(self):
        response = requests.get(f"{self.url}/flavors/detail", headers=self.header)
        if response.status_code == 200:
            flavors = response.json()["flavors"]
            for flavor in flavors:
                if flavor['name'] == "S.4":
                    flavor_id = flavor['id']
                    self.flavor_id = flavor_id

    def create_disk(self):
        volume_url = "https://api-ap-south-mum-1.openstack.acecloudhosting.com:8776/v3/a02b14bcfca64e44bd68f2d00d8555b5/volumes"

        volume_data = {
            "volume": {
                "size": 20,  # Size in GB
                "name": "boot_volume",
                "imageRef": self.image_id,
                "bootable": True,
            }
        }

        response = requests.post(volume_url, json=volume_data, headers=self.header)
        if response.status_code == 202:
            volume = response.json()['volume']
            self.volume_id = volume['id']
            print(self.volume_id)
        else:
            print("Error creating volume:", response.text)



    def get_images(self):
        image_url = "https://api-ap-south-mum-1.openstack.acecloudhosting.com:9292"
        response = requests.get(f"{self.url}/images", headers=self.header)
        #response = requests.get(f"{image_url}", headers=self.header)
        #print(response.status_code)
        #print(response.text)
        images = response.json()["images"]
        for image in images:
            if image['name'] == "Redis-7.4.1-Ubuntu-22.04-LTS":
                self.image_id = image['id']
                print(self.image_id)

    def get_networks(self):
        network_url = "https://api-ap-south-mum-1.openstack.acecloudhosting.com:9696"

        response = requests.get(f"{network_url}", headers=self.header)
        link = response.json()['versions'][0]['links'][0]['href']
        #networks = response.json()["versions"]
        #self.network_id = networks[0]['id']
        net_response = requests.get(f"{link}/networks", headers=self.header)
        #print(net_response.status_code)
        #print(net_response.text)

        networks = net_response.json()["networks"]
        for network in networks:
            if network['name'] == "External_Net_MUM":
                self.network_id = network['id']
                print(self.network_id)
        

    def get_keypairs(self):
        keypair_url = "https://api-ap-south-mum-1.openstack.acecloudhosting.com:9311"
        response = requests.get(f"{keypair_url}", headers=self.header)
        #print(response.status_code)
        #print(response)

        self.keypair = response.json()['versions']['values'][0]['id']
        print(self.keypair)



