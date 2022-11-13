# Printing menu
print("===== CONTACT TRACING ====="
      "\n|          Menu           |"
      "\n|   1 -> Add an item      |"
      "\n|   2 -> Search           |"
      "\n|   3 -> Exit             |"
      "\n===========================")

contact_list = {}

#Main menu options
mainmenu = 0
while mainmenu in (0,1,2,3):
      # Input for menu
      mainmenu = int(input("Choose what to do: "))
      # For Option 1
      if mainmenu == 1:
            print("ADDING AN ITEM:")
            full_name = input("Enter the full name: ")
            age = int(input("Enter your age: "))
            contact_address = input("Enter your address: ")
            phone_number = input("Enter the phone number: ")
            contact_info = [full_name, age, contact_address, phone_number]
            print("Saved!")
            contact_list[full_name] = contact_info
      # For Option 2
      if mainmenu == 2:
            print("SEARCHING FOR AN ITEM:")
            search_key = input("Enter the full name to search: ")
            print(contact_list[search_key])

      # For Option 3
      if mainmenu == 3:
            print("THANK YOU!")
            break





