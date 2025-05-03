class DeleteVM:
    def __init__(self, token, product_id):
        self.token = token

    def delete(self):
        # Logic to delete the VM
        print(f"Deleting VM with ID: {self.vm_id}")
        # Here you would add the actual deletion logic
        return f"VM with ID {self.vm_id} deleted successfully."