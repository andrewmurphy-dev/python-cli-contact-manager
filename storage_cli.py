import json

def save_manager(contacts):
    with open("contacts.json", "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)






