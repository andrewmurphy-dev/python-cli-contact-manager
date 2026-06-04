#here we will implement search contacts! 
#so here we will search contacts ! 


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
    







