import requests
from utils.file import FileHandler
import os

class VolumeCreator:
    def __init__(self, token, size, product_id):
        self.token = token
        self.product_id = product_id
        self.url = "https://api-ap-south-mum-1.openstack.acecloudhosting.com:8776/v3/a02b14bcfca64e44bd68f2d00d8555b5/volumes"
        self.header = {
            "Content-Type": "application/json",
            "X-Auth-Token": self.token
        }
        self.size = size
        self.output_dir = "data/volume_data.json"
        self.file_handler = FileHandler()

    def create_volume(self, volume_name = "data_disk"):
        payload = {
            "volume": {
                "size": self.size,
                "name": volume_name,
                "product_id": self.product_id
            }
        }

        response = requests.post(self.url, headers=self.header, json=payload)

        if response.status_code == 202:
            volume_id = response.json()["volume"]['id']
            if os.path.exists(self.output_dir):
                 vm_data = self.file_handler.load_json(self.output_dir)
                 vm_data.append({
                    "volume_name": volume_name,
                    "volume_id": response.json()["volume"]["id"],
                    "size": self.size,
                })
                 self.file_handler.save_json(vm_data, self.output_dir)
            else:
                 vm_data = [{
                    "volume_name": volume_name,
                    "volume_id": response.json()["volume"]["id"],
                    "size": self.size,
                }]

            self.file_handler.save_json(vm_data, self.output_dir)

            print(f"Volume '{volume_name}' created with ID: {volume_id}")

        else:
            print("Error creating volume:", response.status_code, response.text)

class VolumeDeleter:
    def __init__(self, token, project_id):
        self.token = token
        self.project_id = project_id
        
        self.header = {
            "Content-Type": "application/json",
            "X-Auth-Token": self.token
        }
        self.file_handler = FileHandler()
    
    def delete_volume(self):
        vol_data = self.file_handler.load_json("data/volume_data.json")
        for volume in vol_data:
            volume_id = volume["volume_id"]
            print(f"Volume ID: {volume_id}")
            self.url = f"https://api-ap-south-mum-1.openstack.acecloudhosting.com:8776/v3/0a02b14bcfca64e44bd68f2d00d8555b5/volumes/{volume_id}"
            user_input = int(input("Please enter 1 to delete volume: "))
            if user_input == 1:
                print(f"Deleting volume '{volume_id}'...")
                response = requests.delete(f"{self.url}/{volume_id}", headers=self.header)
                self.file_handler.save_json(vol_data, "data/volume_data.json")
                if response.status_code == 204:
                    print(f"Volume '{volume_id}' deleted successfully")
                    vol_data.remove(volume)
                else:
                    print("Error deleting volume:", response.status_code, response.text)
            else:
                pass

        print("Deletion completed")


