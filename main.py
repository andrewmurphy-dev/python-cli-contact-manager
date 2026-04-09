from auth import add_contact, search_contacts, display_contacts



#add a contact !
#name
#phone
#email address


def cli_manager():
    print("welcome to main menu\n")
    name = input("Enter your name: ")


    while True:
        cli_menu = (f"{name} please enter your choice: ")
        print(cli_menu)
        #press 1 to add contact
        print("press 1: to add contacts\n")
        #press 2 to search contact
        print("press 2: to search contacts\n")
        #press 3 to update contact
        print("press 3: to update contacts\n")
        #press 4 tp delete contact
        print("press 4: to delete contacts\n")
        #press 5 to show contacts
        print("press 5: to display contacts\n")
        # press 'exit to leave
        print("press 6: to exit\n")

        user_inputt = input("-->:  ")
        if user_inputt == "exit":
            print("goodbye")
            break


        

        if user_inputt == "1":
            print("menu: 1 selected")
            add_contact()
        elif user_inputt == "":
            print("menu: option cannot be blank! try again !")

        else:
            print("invalid option")

        if user_inputt == "2":
            print("menu: 2 selected")
            search_contacts()
        elif user_inputt == "":
            print("menu: option cannot be blank! try again !")

        else:
            print("invalid option")

        if user_inputt == "3":
            print("menu: 3 selected")
        elif user_inputt == "":
            print("menu: option cannot be blank! try again !")

        else:
            print("invalid option")

        if user_inputt == "4":
            print("menu: 4 selected")
        elif user_inputt == "":
            print("menu: option cannot be blank! try again !")

        else:
            print("invalid option")


        if user_inputt == "5":
            print("menu: 5 selected")
            display_contacts()
        elif user_inputt == "":
            print("menu: option cannot be blank! try again !")

        else:
            print("invalid option")



cli_manager()
add_contact()
search_contacts()
display_contacts()




#im trying to write this better ! instead of saying print , print , print !


