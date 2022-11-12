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
            contact_info = full_name, age, contact_address, phone_number
            print("Saved!")
            contact_list.append(contact_info)
      # Option 2
      if mainmenu == 2:
            search = []
            for_search = -1
            search_contact = str(input("Type full name to search: "))
            for i in range(len(contact_list)):
                  if search_contact == contact_list[i][0]:
                        for_search = i
                        search.append(contact_list[i])





