import json
from utils.file import FileHandler
from services.query_breakdown import QueryProcessor
from services.vm_creation import VMCreator
from services.vm_deletion import DeleteVM
from services.network_creation import NetworkCreator
from services.volume_operation import VolumeCreator
from services.vm_resizing import VMResizer
from services.volume_operation import VolumeDeleter

file_handler = FileHandler()

while True:
    query = input("Please enter your query (or type 'exit' to quit): ")

    if query.lower() == "exit":
        print("Exiting the system.")
        break

    sage = QueryProcessor(query)
    sage.break_query()
    intent = sage.verify_intent()

    if intent == "VM Provisioning":
        crate = VMCreator(
            "gAAAAABoFhtvDDi_p7bmiHhMIvSYxb6bnR2YN7o7HyWGqbltbOwSpqjvS_4mIA_aOI7ulwPPa5bJmuekTexSjS2xQB4vWyIz53Jd_s0nN4iBGIiiqDy9GNYiQmULPCBJuyMx48IEa1OkCiLFLD0SjIoMmBc8iwQtC9r7H4JVkTvrovMkoHzjecw",
            "0a02b14bcfca64e44bd68f2d00d8555b5"
        )
        crate.get_flavors()
        crate.get_images()
        crate.get_networks()
        crate.get_keypairs()
        crate.create_disk()
        crate.create_vm()

    elif intent == "VM Deletion":
        deleter = DeleteVM(
            "gAAAAABoFhtvDDi_p7bmiHhMIvSYxb6bnR2YN7o7HyWGqbltbOwSpqjvS_4mIA_aOI7ulwPPa5bJmuekTexSjS2xQB4vWyIz53Jd_s0nN4iBGIiiqDy9GNYiQmULPCBJuyMx48IEa1OkCiLFLD0SjIoMmBc8iwQtC9r7H4JVkTvrovMkoHzjecw",
            "0a02b14bcfca64e44bd68f2d00d8555b5"
        )
        with open("data/vm_data.json", 'r') as file:
            data = json.load(file)
            if isinstance(data, list) and not data:
                print("The file contains an empty JSON array.")
            else:
                print("The file does not contain an empty JSON array.")
                deleter.delete()

    elif intent == "Network Creation":
        net_creator = NetworkCreator(
            "gAAAAABoFhtvDDi_p7bmiHhMIvSYxb6bnR2YN7o7HyWGqbltbOwSpqjvS_4mIA_aOI7ulwPPa5bJmuekTexSjS2xQB4vWyIz53Jd_s0nN4iBGIiiqDy9GNYiQmULPCBJuyMx48IEa1OkCiLFLD0SjIoMmBc8iwQtC9r7H4JVkTvrovMkoHzjecw"
        )
        net_creator.create_network()

    elif intent == "Volume Operations":
        size = int(input("Please enter size of volume: "))
        vol_create = VolumeCreator(
            "gAAAAABoFhtvDDi_p7bmiHhMIvSYxb6bnR2YN7o7HyWGqbltbOwSpqjvS_4mIA_aOI7ulwPPa5bJmuekTexSjS2xQB4vWyIz53Jd_s0nN4iBGIiiqDy9GNYiQmULPCBJuyMx48IEa1OkCiLFLD0SjIoMmBc8iwQtC9r7H4JVkTvrovMkoHzjecw",
            size,
            "0a02b14bcfca64e44bd68f2d00d8555b5"
        )
        vol_create.create_volume()

    else:
        print("Invalid intent. Please try again.")

