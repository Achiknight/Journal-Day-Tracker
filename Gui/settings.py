from Gui.GRoot import *
from utility.Wid_Snip import *
from Backend.Pallet_Change import color_change,reload_widget_colors
import json


created = False

def reload_fr(key,rot):
    color_change(key)
    reload_widget_colors(rot)

class Settings():
    
    def Pall_data():
        file = open("Config.json","r")
        data = json.load(file)
        palette = data["palettes"]
        file.close()
        return palette
    
    def Pallet(Frame):
        ipr = 2
        Row = CTkFrame(Frame,fg_color=fg)
        Row.pack(fill="x")
        data = Settings.Pall_data()
        for index,key in enumerate(data.keys()):
            if index % ipr == 0 and index != 0:
                Row = CTkFrame(Frame,fg_color=fg)
                Row.pack(fill="x")
            cur = data[key]
            Block = CTkFrame(Row, fg_color=fg, width=200, height=100)
            Block.pack(side='left',padx=(0,20))
            change = Button(Block,command=lambda i=key,e=root: reload_fr(i,e))
            change.configure(text="Change")
            change.pack()
            
            pal_name = LabelBody(Block)
            pal_name.pack()
            pal_name.configure(text=key)
            for keys in cur.keys():
                if keys == "Font_style1" or keys == "Font_style2":
                    continue
                CTkLabel(Block,text=keys,text_color=cur[keys]).pack()




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
        
        
        
        # cenge = Button(setts)
        # cenge.configure(text="Change",command=lambda:color_change("vintage_editorial"))


        # relo = Button(setts)
        # relo.configure(text="Reload",command=lambda:reload_widget_colors(root))
        created = True
        frm = CTkScrollableFrame(setts,fg_color=fg)
        frm.pack(fill="both",expand=True)
        
        Settings.Pallet(frm)
