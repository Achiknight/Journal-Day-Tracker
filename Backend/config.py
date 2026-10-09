import json
var_list =  {"background_color": "fg", "hover_color": "hv", "text_color": "txt", "border_color": "brd", "Font_style1": "Ft1", "Font_style2": "Ft2"}
def color_var():           #! 
    file = open(r"Config.json","r")

    data = json.load(file)
    pallet = data["palettes"]
    current = pallet["current"]
        
    file.close()


    for keys in current.keys():
        globals()[var_list[keys]] = current[keys]


color_var()