#so here we will focus on changing the add contact 

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

    
    
        

    



