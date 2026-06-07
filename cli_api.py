from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from storage_cli import load_manager

app = FastAPI() 

class ContactData(BaseModel):
    name: str = Field(Min_length=1)
    phone: str = Field(min_length=6)
    email: str = Field(Min_length=1)





@app.get("/")
def home():
    return {"message": "FastAPI is working!"}




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
    email = email.lower().strip()

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



@app.patch("/contact/{current_email}")
def update_contact(current_email: str, update_data: ContactData):

    final_data = update_data.model_dump(exclude_none=True)




    if final_data == {}:
        raise HTTPException(status_code=400, detail="no data provided!")
        
    
    for characters in contact:
        if characters["email"] == "current_email":


            if "name" in final_data:
                contact["name"] = update_data["name"]

            if "phone" in final_data:
                contact["phone"] = update_data["phone"]

            if "email" in final_data:
                contact["phone"] = update_data["phone"]

            return {
                "message": "update contact updated successfully!",
                "contact": contact
            }
        
        raise HTTPException(status_code=404, detail="contact not found!")






@app.delete("/contact")
def delete_contact(email: str):
    for contacts in contact:
        if contact["email"] == email:
            contact.remove(contacts)

            return {
                "message": "Contact deleted successfully",
                "contact": contact
            }

    raise HTTPException(status_code=404, detail="Contact not found")



    
    

    




    
    








