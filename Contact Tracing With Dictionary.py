# Printing menu
print("Contact Tracing"
      "\nMenu: "
      "\n1 -> Add an item"
      "\n2 -> Search"
      "\n3 -> Exit")

contact_age = {
      "Chantal Saballo": 20
      "Dominique Crespo": 19
}
contact_address = {
      "Chantal Saballo": Padilla
      "Dominique Saballo": Lower Antipolo
}
contact_number = {
      "Chantal Saballo": 0995
      "Dominique Saballo": 0956
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
            print("Saved!")
      # For Option 2
      if mainmenu == 2:






