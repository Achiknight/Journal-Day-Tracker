import json
from DBFile.Connection import sql3,Mysql

dbchoice = {"sql3":sql3,"mysql":Mysql}
var_list =  {"background_color": "fg", "hover_color": "hv", "text_color": "txt", "border_color": "brd", "Font_style1": "Ft1", "Font_style2": "Ft2"}


def color_var():           #! 
    file = open(r"Config.json","r")

    data = json.load(file)
    pallet = data["palettes"]
    current = pallet["current"]
        
    file.close()


    for keys in current.keys():
        globals()[var_list[keys]] = current[keys]


#?#############################################################
#*#############################################################
#!#############################################################


def cusor_():
    file = open(r"Config.json","r")
    
    file_data = json.load(file)
    file.close()
    
    dbs = file_data["dbchoice"]
    choice = dbs["choice"]
    
    if choice not in ["sql3","mysql"]:
        choice = "sql3"
    
    match(choice):
        case "sql3":
            data,cur = dbchoice[choice]()
        case "mysql":
            creds = file_data["dbchoice"]["info"]
            data,cur, _ = dbchoice[choice](creds["host"],creds["username"],creds["password"],creds["database"])
    return data,cur

color_var()