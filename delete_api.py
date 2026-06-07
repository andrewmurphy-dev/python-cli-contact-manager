

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



    