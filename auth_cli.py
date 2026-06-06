
from storage_cli import contacts

def add_contact_api():
    print()
    print("Welcome to add contact section!")

    name = input("Please enter your name: ").strip().lower()

    if name == "":
        print("name cannot be blank!")
        return 
    
    email = input("Please enter your email: ").strip().lower()

    if email == "":
        print("email must not be blank!")


    phone = input("Please enter your phone number: ").strip()

    if len(phone) < 8:
        print("phone is too short!")
        return 
    
    #we want the number to be a string !but we want it to be digit strings !
    #not character stirngs !
    

    for character in phone:
       if not character.isdigit():
           print("phone number must be digits!")
           return 
       

    contacts = {
        "name": name,
        "email": email,
        "phone": phone
    }
       

    try:
        response = request.post(f"{BASE_URL}/contact",
                                json = {"name": name, 
                                        "email": email,
                                        "phone": phone}
                                        , timeout=10
                    
                                )
        

        response.raise_for_status()
        data = response.json()
        print(data["message"])





#day 2

def display_contacts():

    try:
        response = requests.get(f"{BASE_URL}/Contact", Timeout=10)

        response.raise_for_status()

        for contact_key, contact_value in contact.items():
            print("name:", contact_value["name"])
            print("phone:", contact_value["phone"])
            print("email:", contact_value["email"])
            print()

    
    except requests.exceptions.ConnectionError:
        print("connection to the server was not viable!")
        return 


    except request.exceptions.Timout:
        print("error: server timout exceeded!")
        return


    except request.exceptions.HTTPerror as error:
        print(f"error: server has returned {error}")
        return


    except request.exceptions.RequestException:
        print("error: server request failed!")
        return


    except ValueError:
        

    




def search_contacts():
    print() 
    print("welcome to search contacts!")

    email = input("enter the associated email address of the user in which you want to search: ")


    try:
        response = requests.get(f"{BASE_URL}/contacts/{email}", timeout=10,
                               json = {
                                   "email": email
                               }
        )

        response.raise_for_status()

        data = response.json() 
        print(data)
        
    
    except requests.exceptions.Connection.Error:
        print("error: unable to connect to server")
        return 
    

    except requests.exception.Timeout:
        print("error: the server has exceeded the timeout!")
        return 


    except requests.exception.HTTPerror as error:
        print(f"error: the server has an {error}")
        return 
    
    except requests.exception.Request.Exception:
        print("error: server request failed!")
        return 






def delete_contact():
    print()
    print("welcome to delete contact section!")

    email = input("Enter the user email you wish to delete!: ").strip()

    try:
        response = requests.delete(f"{BASE_URL}/contact", timeout=10, 
                                   json = {
                                       "email": email
                                   })
        
        response.raise_for_status()

        data = response.json()
        print(data)


    except requests.exceptions.ConnectionError:
        print("error: there is an error with connecting to the server!")
        return
    
    except requests.exception.Timeout:
        print("error: the server connection has exceeded the timeout!")
        return 

    except requests.exception.HTTPerror as error:
        print(f"error: Server has an {error}")
        return 

    except requests.exception.Request.Exception:
        print("error: server request failed!")
        return 










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



             if choice == "2":
                new_email = input("please enter new email: ").lower().strip()
                #this follows a different structure
                value["email"] = new_email
                print("email updated")


            elif choice == "":
                print("menu: option cannot be blank! try again !")

            else:
                print("invalid option")



            if choice == "3":
                new_phone = input("please enter new phone number: ").lower().strip()
                value["phone"] = new_phone
                print("phone updated")

            elif choice == "":
                print("menu: option cannot be blank! try again !")

            else:
                print("invalid choice")
            break

    




    else:
        print("not found")







