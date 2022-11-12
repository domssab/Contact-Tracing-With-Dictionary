# Printing menu
print("Contact Tracing"
      "\nMenu: "
      "\n1 -> Add an item"
      "\n2 -> Search"
      "\n3 -> Exit")

contact_list = []
#Main menu options
mainmenu = 0
while mainmenu in (0,1,2,3):
      # Input for menu
      mainmenu = int(input("Choose what to do: "))
      if mainmenu == 1:
            contact_info = []
            full_name = input("Enter the full name: ")
            age = int(input("Enter your age: "))
            contact_address = input("Enter your address: ")
            phone_number = input("Enter the phone number: ")
            contact_info = [full_name, age, contact_address, phone_number]
            print("Here's the contact info:", contact_info)
            contact_list.append(contact_info)
            return contact

