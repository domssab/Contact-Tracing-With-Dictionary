# Printing menu
print("Contact Tracing"
      "\nMenu: "
      "\n1 -> Add an item"
      "\n2 -> Search"
      "\n3 -> Exit")

#Main menu options
mainmenu = 0
while mainmenu in (0,1,2,3)
      # Input for menu
      mainmenu = int(input("Choose what to do: "))
      if mainmenu == 1:
            contact_info = []
            full_name = input("Enter the full name: ")
            age = int(input("Enter your age: "))
            address = input("Enter your address: ")
            phone_number = input("Enter the phone number: ")