#so here we want to display contcts 
#we know contacts is a nested dictionary ! 
#so remmeber we use get response ! 
#we use try for get response 

#so waht error and validation we need 
#call_to_status()? ---> raise_to_status()
#so its not call its raise !
#also its for ! 
#so raise_for_status()
#this gives a http resposne object status code if the server is down. 


#how do we loop over a nested dictiionary 
#nested loop 

#but in this case we can just do 
#for contact_id, contact_value in contact.items()






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
        




   


