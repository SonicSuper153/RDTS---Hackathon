import requests

class VMResizer:
    def __init__(self, token, project_id):
        self.token = token
        self.project_id = project_id
        self.header = {
            "X-Auth-Token": self.token,
            "Content-Type": "application/json"
        }
        self.base_url = f"https://api-ap-south-mum-1.openstack.acecloudhosting.com:8774/v2.1/{self.project_id}/servers"

    def resize_vm(self, vm_id, new_flavor_id):
        """
        Initiates a resize of the VM to a new flavor.
        """
        resize_url = f"{self.base_url}/{vm_id}/action"
        data = {
            "resize": {
                "flavorRef": new_flavor_id
            }
        }

        response = requests.post(resize_url, json=data, headers=self.header)
        if response.status_code == 202:
            print(f"Resize initiated successfully for VM {vm_id}")
        else:
            print("Failed to resize VM:", response.status_code, response.text)

    def confirm_resize(self, vm_id):
        """
        Confirms the resize operation after it has entered VERIFY_RESIZE state.
        """
        confirm_url = f"{self.base_url}/{vm_id}/action"
        data = { "confirmResize": None }

        response = requests.post(confirm_url, json=data, headers=self.header)
        if response.status_code == 204:
            print(f"Resize confirmed for VM {vm_id}")
        else:
            print("Failed to confirm resize:", response.status_code, response.text)

    def revert_resize(self, vm_id):
        """
        Reverts a resize if needed.
        """
        revert_url = f"{self.base_url}/{vm_id}/action"
        data = { "revertResize": None }

        response = requests.post(revert_url, json=data, headers=self.header)
        if response.status_code == 202:
            print(f"Resize reverted for VM {vm_id}")
        else:
            print("Failed to revert resize:", response.status_code, response.text)
