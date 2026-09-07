import json
from Backend.config import color_var
from Backend.config import fg,txt,Ft1,Ft2,brd,hv

file = open("Config.json", "r")
data = json.load(file)
file.close()

pallet = data["palettes"]

def color_change(chosen):
    pallet["current"] = pallet[chosen]
    
    file = open("Config.json", "w")
    json.dump(data, file, indent=4)
    file.close()
    color_var()
    
def reload_widget_colors(widget):
    try:
        widget.configure(fg_color=fg)
    except:
        pass

    try:
        widget.configure(text_color=txt)
    except:
        pass

    try:
        widget.configure(hover_color=hv)
    except:
        pass

    try:
        widget.configure(border_color=brd)
    except:
        pass

    for child in widget.winfo_children():
        reload_widget_colors(child)
    print("Called")
