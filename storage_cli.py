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



contacts = load_manager()


#you forgot some things here
#for some reason in another project u didnt put json.load(file) in stoage
#both can work but the problem is u will have mutple storage dictionaries in memory



#The real difference
#main.py version
#main.py knows about JSON
#main.py knows about the file name
#main.py opens the file
#main.py saves the file
#storage.py version
#main.py does not care about JSON details
#main.py just calls save_users(users)
#storage.py handles the file wo



