import json

def check_name():
    file = open(r"Config.json","r")

    data = json.load(file) 
    user = data["USER"]
    if user["Name"] == "":
        return False
    else:
        return True