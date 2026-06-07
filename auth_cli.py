import requests



BASE_URL = "http://127.0.0.1:8000"



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
        return


    phone = input("Please enter your phone number: ").strip()

    if len(phone) < 8:
        print("phone is too short!")
        return 
    
    

    for character in phone:
       if not character.isdigit():
           print("phone number must be digits!")
           return 
       

    contact = {
        "name": name,
        "email": email,
        "phone": phone
    }
       

    try:
        response = requests.post(f"{BASE_URL}/contact",
                                json=contact
                                        , timeout=10
                     )
        

        response.raise_for_status()

        data = response.json()
        print(data["message"])


    except requests.exceptions.ConnectionError:
        print("error: there is a connection issue!")
        return 
    
    except requests.exceptions.Timeout:
        print("error: the connections to server has excceded 10 seconds!")
        return 
    
    except requests.exceptions.HTTPError as error:
        print(f"error: the server has an {error}")
        return
    
    except requests.exceptions.RequestException:
        print("error: there is a error sending request!")

    except ValueError:
        print("the server did not return valid JSON!")
        return 






def display_contacts():

    try:
        response = requests.get(f"{BASE_URL}/Contact", Timeout=10)

        response.raise_for_status()

        data = response.json()
        print(data["message"])

        for contact_key, contact_value in contact.items():
            print("name:", contact_value["name"])
            print("phone:", contact_value["phone"])
            print("email:", contact_value["email"])
            print()

    
    except requests.exceptions.ConnectionError:
        print("connection to the server was not viable!")
        return 


    except requests.exceptions.Timout:
        print("error: server timout exceeded!")
        return


    except requests.exceptions.HTTPError as error:
        print(f"error: server has returned {error}")
        return


    except requests.exceptions.RequestException:
        print("error: server request failed!")
        return


    except ValueError:
        print("the server did not return the valid JSON type")
        return 
        

    


def search_contacts():
    print() 
    print("welcome to search contacts!")

    email = input("enter the associated email address of the user in which you want to search: ").strip()

    if email == "":
        print("email cannot be blank!")
        return 
    
    if "@" not in email:
        print("email does not contain @!, try again! ")
        return 
    
    if len(email) < 8:
        print("email is too short! try again!")
        return 


    try:
        response = requests.get(f"{BASE_URL}/contacts/{email}", timeout=10,
                               )
        

        response.raise_for_status()

        data = response.json() 
        print(data["message"])
        
    
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
    
    except ValueError:
        print("server did not send the valid JSON type")
        return






def delete_contact():
    print()
    print("welcome to delete contact section!")

    email = input("Enter the user email you wish to delete!: ").strip()

    if email == "":
        print("email must not be blank!")
        return
    
    if "@" not in email:
        print("email is invalid!")
        return


    try:
        response = requests.delete(f"{BASE_URL}/contact/{email}", timeout=10, 
                                  )
        
        response.raise_for_status()

        data = response.json()
        print(data["message"])


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
    
    except ValueError:
        print("the response of the server is a invalid JSON type!")
        return 





def update_contact():
    print()
    print("welcome to update contact!")


    while True:
        current_email = input("enter the email assoicated with the user you wish to change!: ").strip()

        if current_email == "":
            print("email is blank! try again!")
            return
        
        if "@" not in current_email:
            print("email is invalid!")
            return



        print("choose from the following you wish to update!")

        print("press 1: email")
        print("press 2: phone")
        print("press 3: name")

        option = input("choose a option: ")

        if option == "":
            print("option must not be blank!")
            return
        
        if len(option) > 1:
            print("invalid input!")
            return 



        update_data = {}

        if option == "1":
            new_email = input("enter the new email you want to change too!: ").strip()
            update_data["email"] = new_email 

            if new_email == "":
                print("email cannot be blank!")
                continue

            elif "@" not in new_email:
                print("email is invalid!")
                continue


        elif option == "2":
            new_phone = input("enter the new phone you want to change too!: ").strip()
            update_data["phone"] = new_phone 

            if new_phone == "":
                print("phone cannot be blank!")
                continue

            elif len(new_phone) < 8:
                print("phone is too short")
                continue


        elif option == "3":
            new_name = input("enter the new name you want to change too!: ").strip()
            update_data["name"] = new_name

            if new_name == "":
                print("new name cannot be blank!")
                continue


        try:
            response = requests.post(f"{BASE_URL}/contact/{current_email}",
                                     json=update_data, 
                                     timeout=10
                                    )
            
            response.raise_for_status()

            data = response.json()

            print(data["message"])


        except requests.exceptions.ConnectionError:
            print("error: unale to connect to server!")
            return 
        
        except requests.exceptions.HTTPError as error:
            print(f"error: there is an server {error}")
            return
        

        except requests.exceptions.Timeout:
            print("error: server has exceeded timeout!")

        except requests.exceptions.RequestException:
            print("error: server request failed!")
            return 
        
        except ValueError:
            print("the response of the server is a invalid JSON type!")
            return 








