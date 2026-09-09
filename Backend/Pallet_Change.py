import json
from Backend import config

file = open("Config.json", "r")
data = json.load(file)
file.close()

pallet = data["palettes"]

def color_change(chosen):
    pallet["current"] = pallet[chosen]
    
    file = open("Config.json", "w")
    json.dump(data, file, indent=4)
    file.close()
    config.color_var()
    
def reload_widget_colors(widget):
    try:
        widget.configure(fg_color=config.fg)
    except:
        pass

    try:
        widget.configure(text_color=config.txt)
    except:
        pass

    try:
        widget.configure(hover_color=config.hv)
    except:
        pass

    try:
        widget.configure(border_color=config.brd)
    except:
        pass

    for child in widget.winfo_children():
        reload_widget_colors(child)
                
