# Printing menu
print("Contact Tracing"
      "\nMenu: "
      "\n1 -> Add an item"
      "\n2 -> Search"
      "\n3 -> Exit")

contact_list = {
      "Chantal Saballo": [20, "Padilla", 9954],
      "Dominique Crespo": [19, "Lower Antipolo", 9653]
}

#Main menu options
mainmenu = 0
while mainmenu in (0,1,2,3):
      # Input for menu
      mainmenu = int(input("Choose what to do: "))
      # For Option 1
      if mainmenu == 1:
            full_name = input("Enter the full name: ")
            age = int(input("Enter your age: "))
            contact_address = input("Enter your address: ")
            phone_number = input("Enter the phone number: ")
            contact_info = ["Name:", full_name,
                            "\nAge:", age,
                            "\nAddress: ", contact_address,
                            "\nPhone Number: ", phone_number]
            print("Saved!")
            contact_list[full_name] = contact_info
      # For Option 2
      if mainmenu == 2:
            search_key = input("Enter the full name to search: ")
            print(contact_list[search_key])

      # For Option 3
      if mainmenu == 3:
            break





