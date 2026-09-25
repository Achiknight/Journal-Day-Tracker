import json

def check_name():
    file = open(r"Config.json","r")

    data = json.load(file) 