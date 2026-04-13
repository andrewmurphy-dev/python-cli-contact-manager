
from storage_cli import contacts


def add_contact():
    name = input("Please enter your name: ").strip().lower()
    email = input("Please enter your email: ").strip().lower()
    phone = input("Please enter your phone number: ").strip().lower()

#what happens if the user types nothing ??

    contacts[name] = {"email": email, "phone": phone}
    print(contacts)


#day 2

def display_contacts():
    print("welcome to display contacts!")
    variable = input("menu: please enter your choice")
    print("press 1: \tto view all users")
    



    #day 3
def search_contacts():
    print("wecome to search menu")
    email = input("menu: please enter the email address associated with user: ")
    for name, value in contacts.items():
        if email == value["email"]:
            print("username:\t", name)
            print("email:\t", value["email"])
            print("phone:\t", value["phone"])
            break
    else:
         print("not found")

        #what happens if the user types


def delete_contact():
    print("welcome to delete contact")
    name = input("please enter the username you want to delete: ")
    if name in contacts:
        del contacts[name]
        print("contact deleted")
    else:
        print("not found")











#update contact
def update_contact():
    print("welcome to update contact")
    email = input("type the email address associated with user: ")
    for name, value in contacts.items():
        if email == value["email"]:
            print("username:\t", name)
            print("email:\t", value["email"])
            print("phone:\t", value["phone"])



            #choosing option

            print("what do you want to update?\n")
            print("press 1: \tto update username")
            print("press 2: \tto update email")
            print("press 3: \tto update phone")

            choice = input("please enter your choice: ")

            if choice == "1":
                new_username = input("please enter new username: ")
                contacts[new_username] = contacts[name]
                del contacts[name]
                print("contact updated")

            elif choice == "":
                print("menu: option cannot be blank! try again !")
                
            else:
                print("invalid option")





            elif choice == "3":
                new_phone = input("please enter new phone number: ")
                value["phone"] = new_phone
                print("phone updated")

            else:
                print("invalid choice")
            break


    else:
        print("not found")







