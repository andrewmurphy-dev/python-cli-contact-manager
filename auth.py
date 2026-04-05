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



def delete_contact():
    print("welcome to delete contact\n")
    name = input("please enter the username you want to delete: ")
    if name in contacts:
        del contacts[name]
        print("contact deleted")
    else:
        print("not found")




