from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from storage_cli import load_manager, save_manager 

app = FastAPI() 

class ContactData(BaseModel):
    name: str = Field(Min_length=1)
    phone: str = Field(min_length=6)
    email: str = Field(Min_length=1)





BASE_URL = "http://127.0.0.1:8000"

@app.get("/")
def home():
    return {"message": "FastAPI is working!"}




#so display contacts
#so we use get contacts 

@app.get("/contact")
def contact():
    contacts = load_manager()
    return contacts





@app.post("/contact")
def upload_contact(contact: ContactData):
    contacts = load_manager()

    name = contact.name.strip()

    if name == "":
        raise HTTPException(status_code=400, detail="contact name cannot be empty!")
    
    if name in contacts:
        raise HTTPException(status_code=409, detail ="contact already exists!")



    contacts[contact.name] = {
        "phone": contact.phone,
        "email": contact.email
    }

    save_contact(contacts)


    return {
        "message": "Contact added",
        "name": name,
        "phone": contact.phone,
        "email": contact.email
    }




@app.post("/contact/{email}")
def get_contact_email(email: str):
    email = email.lower().strip(9)

    if not isinstance(email, str):
        print("email is the wrong type!")
        return 
    
    if email == "":
        print("email cannot be blank!")
        return 
    
    if "@" not in email:
        print("invalid email")
        return
    

    if email not in contact:
        print("email not found in contacts")
        return 
    
    for contact_id, contact_value in contact.items():
        if email == contact["email"]:
            print("name:", contact_value["name"])
            print("phone:", contact_value["phone"])
            print("email:", contact_value["email"])
            print()


    return  {
        "message": "email found",
        "name": contact.name,
        "phone": contact.phone,
        "email": contact.email
    }





    
    

    




    
    








