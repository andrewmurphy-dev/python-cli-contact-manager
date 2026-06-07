

def update_contact():

    print()
    print("welcome to update contact!")


    while True:
        current_email = input("enter the email assoicated with the user you wish to change!: ").strip()

        print("choose from the following you wish to update!")

        print("press 1: email")
        print("press 2: phone")
        print("press 3: name")

        option = input("choose a option: ")

        update_data = {}

        if option == 1:
            new_email = input("enter the new email you want to change too!: ").strip()
            update_data["email"] = new_email 

            if new_email == "":
                print("email cannot be blank!")
                continue

            elif "@" not in new_email:
                print("email is invalid!")
                continue


        elif option == 2:
            new_phone = input("enter the new phone you want to change too!: ").strip()
            update_data["phone"] = new_phone 

            if new_phone == "":
                print("phone cannot be blank!")
                continue

            elif len(new_phone) < 8:
                print("phone is too short")
                continue


        elif option == 3:
            new_name = input("enter the new name you want to change too!: ").strip()
            update_data["name"] = new_name

            if new_name == "":
                print("new name cannot be blank!")
                continue


        try
            response = requests.post(f"/{BASE_URL}/contacts/{current_email}",
                                     json=update_data, 
                                     timeout=10
                                    )
            
            response.raise_for_status()


        except requests.exceptions.ConnectionError:
            print("error: unale to connect to server!")
            return 
        
        except requests.exceptions.HTTPerror as error:
            print(f"error: there is an server {error}")
            return
        

        except requests.exceptions.Timeout:
            print("error: server has exceeded timeout!")

        except requests.exceptions.Request.Exceptions:
            print("error: server request failed!")
            return 

