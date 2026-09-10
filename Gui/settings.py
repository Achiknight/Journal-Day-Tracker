from Gui.GRoot import *
from utility.Wid_Snip import *
from Backend.Pallet_Change import color_change,reload_widget_colors
import json


created = False

class Settings():
    
    def Pall_data():
        file = open("Config.json","r")
        data = json.load(file)
        palette = data["palettes"]
        file.close()
        return palette
    
    def Pallet(setts):
        ipr = 2
        Row = CTkFrame(setts,fg_color=fg)
        Row.pack()
        data = Settings.Pall_data()
        for index,key in enumerate(data.keys()):
            if index == 0:
                pass
            if index % ipr == 2:
                Row = CTkFrame(setts,fg_color=fg)
                Row.pack()
            cur = data[key]
            Block = CTkFrame(Row,fg_color=fg)
            for keys in cur.keys():
                if keys == "Font_style1" or keys == "Font_style2":
                    continue
                CTkLabel(Block,text=keys,text_color=cur[keys]).pack()
            print(index)
            
        


    def Create(master):
        global created
        if created:
            return
        setts = CTkToplevel(master) 
        setts.geometry("580x520")
        setts.config(background=fg)
        Head = LabelHead(setts)
        Head.configure(text="Settings")
        Head.pack()
        
        
        Settings.Pallet(setts)
        
        cenge = Button(setts)
        cenge.configure(text="Change",command=lambda:color_change("vintage_editorial"))


        relo = Button(setts)
        relo.configure(text="Reload",command=lambda:reload_widget_colors(root))
        created = True
        Settings.Pallet(setts)
