from storage import contacts



def add_contact():
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    phone = input("Please enter your phone number: ")

    #so day 1 understanding is how do we implement this data into the contacts dictionary !

    contacts[name] = {"email": email, "phone": phone}
    print(contacts)


#day 2

def display_contacts():
    for key, value in contacts.items():
        print(key, value)



    #day 3
def search_contacts():
    print("wecome to search menu\n")
    email = input("menu: please enter the email address associated with user: ")
    for name, value in contacts.items():
        if email == value["email"]:
            print("username:\n", name)
            print("email:\n", value["email"])
            print("phone:\n", value["phone"])
        else:
            print("not found")


def delete_contact():
    print("welcome to delete contact\n")
    name = input("please enter the username you want to delete: ")
    if name in contacts:
        del contacts[name]
        print("contact deleted")
    else:
        print("not found")

def update_contact():
    print("welcome to update contact\n")
    email = input("type the email address associated with user: ")
    for key, value in contacts.items():
        if email == value["email"]:
            print("username:\n", key)
            print("email:\n", value["email"])
            print("phone:\n", value["phone"])

            print("what do you want to update?\n")
            print("press 1: to update username")
            print("press 2: to update email")
            print("press 3: to update phone")

            choice = input("please enter your choice: ")

            if choice == "1":
                new_username = input("please enter new username: ")

                contacts[new_username] = contacts[name]
                del contacts[name]

                print("contact updated")


            elif choice == "2":
                new_email = input("please enter new email: ")



