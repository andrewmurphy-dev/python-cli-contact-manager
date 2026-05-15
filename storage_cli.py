import json

def save_manager(contacts):
    with open("contacts.json", "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)



def load_manager():
    try:
        with open("contacts.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("no file found")
        return {}

    except json.JSONDecodeError:
        print("error the file type is not json format")
    return None









