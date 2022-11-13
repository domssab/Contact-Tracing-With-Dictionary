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
      # Option 1
      if mainmenu == 1:
            contact_info = []
            full_name = input("Enter the full name: ")
            age = int(input("Enter your age: "))
            contact_address = input("Enter your address: ")
            phone_number = input("Enter the phone number: ")
            contact_info = [full_name, age, contact_address, phone_number]
            print("Saved!")
            contact_list.append(contact_info)
      # Option 2
      if mainmenu == 2:
            for_search = int(input("1. Full name"
                                   "\n 2. Address"
                                   "\n 3. Phone Number"
                                   "\n Which to search? "))
            search = []
            to_search = -1
            if for_search == 1:
                  full_name_search = str(input("Type full name to search: "))
                  for f in range(len(contact_list)):
                        if full_name_search == contact_list[f][0]:
                              to_search = f
                              search.append(contact_list[f])

            elif for_search == 2:
                  address_search = str(input("Type full address to search: "))
                  for a in range(len(contact_list)):
                        if address_search == contact_list[a][1]:
                              to_search = a
                              search.append(contact_list[a])

            elif for_search == 3:
                  phone_number_search = str(input("Type the phone number to search: "))
                  for p in range(len(contact_list)):
                        if phone_number_search == contact_list[p][2]:
                              to_search = p
                              search.append(contact_list[p])

            else:
                  print("Invalid, please try again.")

      # Option 3
      if mainmenu == 3:
            break





