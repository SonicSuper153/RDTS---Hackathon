from utils.file import FileHandler
import requests

class DeleteVM:
    def __init__(self, token, product_id):
        self.token = token
        self.product_id = product_id
        self.file_handler = FileHandler()
        self.vm_data = self.file_handler.load_json("data/vm_data.json")    
        self.header = {
            "X-Auth-Token": self.token,
            "Content-Type": "application/json"
        }


    def delete(self):
        for i in self.vm_data:
            print(f"VM IF->{i['vm_id']}")
            #id_list.append(i['vm_id'])

        input_vm = int(input("Please enter the VM ID you want to delete by its serial number: "))
        self.vm_id = self.vm_data[input_vm-1]['vm_id']
        self.vm_data.pop(input_vm-1)
        self.file_handler.save_json(self.vm_data, "data/vm_data.json" )
    
        self.url = f"https://api-ap-south-mum-1.openstack.acecloudhosting.com:8774/v2.1/a02b14bcfca64e44bd68f2d00d8555b5/servers/{self.vm_id}"

        response = requests.delete(self.url, headers=self.header)

        if response.status_code in [202, 204]:
            print(f"Server {self.vm_id} deleted successfully.")
        else:
            print(f"Error deleting server: {response.text}")
            print(f"Error deleting server: Status Code {response.status_code} - {response.text}")