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
    question_1 = input("menu: please enter the email address associated with user: ")
    for key, value in contacts.items(): #maybe i can do a functuin call to display contacts !
        if question_1 == value["email"]:
            print(key, value)
        else:
            print("not found")


#we need to write this better cause looping will create messy data and it will not look neat !





