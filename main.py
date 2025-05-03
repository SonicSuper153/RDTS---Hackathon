from services.query_breakdown import QueryProcessor
from services.vm_creation import VMCreator

#query = input("Please enter your query: ")
#
#sage = QueryProcessor(query)
#sage.break_query()
#intent = sage.verify_intent()
#
#if intent == "VM Proviisioning":
#    print("Intent classified successfully!")
#
#elif intent == "VM Deletion":
#    print("Intent classified successfully!")
#
#elif intent == "VVM Resizing":
#    print("Intent classified successfully!")
#
#elif intent == "Network Creation":
#    print("Intent classified successfully!")
#
#elif intent == "Volume Operations":
#    print("Intent classified successfully!")
#
#elif intent == "Vsage Query":
#    print("Intent classified successfully!")
#
#else:
#    print("Invalid intent. Please try again.")

crate = VMCreator("gAAAAABoFfsrDLcHbuHU32hwJAnfLKM1eWrF2Xg-dE4MyNxnJeRXGic4CAGq63_-pYtVDuOhFC5cBNZUBQ0hJQr7BaGSP53HeZELfG5tZP_NNJg-IiHhhat7pdnSP0DnOKyK4Ah2aw0h9l9ZHDIICcfee5vjzLbtEd3pw57WhMaS843gejkTXDI", "0a02b14bcfca64e44bd68f2d00d8555b5")
crate.get_flavors()
crate.get_images()
crate.get_networks()
crate.get_keypairs()
crate.create_disk()
#crate.wait_for_volume_available()
crate.create_vm()

