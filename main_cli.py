from auth_cli import add_contact,search_contacts,display_contacts



def cli_manager():
    print("welcome to main menu\n")


    while True:
        square_box("Main Menu", [
            "1. add contacts",
            "2. search contacts",
            "3. update contacts",
            "4. delete contacts"
            "5. display contacts"
            "type exit Logout"
        ])

        option_text = input("enter a option: ").strip()

        if option_text == "":
            print("option cannot be empty!")
            continue

        try:
            option = int(option_text)

        except ValueError:
            print("option must be a number!")
            continue

        if option == "1":
            #function call

        elif option == "2":
            #function call

        elif option == "3":
            #function call

        elif option == "4":
            #function call

        elif option == "5":
            #function call






cli_manager()
add_contact()
search_contacts()
display_contacts()


#im trying to write this better ! instead of saying print , print , print !


