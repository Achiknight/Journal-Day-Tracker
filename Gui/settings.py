from Gui.GUI_Root import *
from utility.Wid_Snip import *
from Backend.Pallet_Change import color_change,reload_widget_colors
import json

idt = None
created = False

dropped = {}

def reload_fr(key,rot,skip):
    color_change(key)
    reload_widget_colors(rot,skip)

  

class Settings():
    # def __init__(self):
        
    
    def drop_setts(frm):
        global dropped
        
        if dropped[frm] == 0:
            frm.pack()
            dropped[frm] = 1
        
        elif dropped[frm] == 1:
            frm.pack_forget()
            dropped[frm] = 0
            
        

    def Root():
        setts = CTkToplevel(root)
        return setts    
    
    
    def Pall_data():
        file = open("Config.json","r")
        data = json.load(file)
        palette = data["palettes"]
        file.close()
        return palette
    
    
    def Pallet(Frame):
        ipr = 2

        
        data = Settings.Pall_data()
        for index,key in enumerate(data.keys()):
            
            if index % ipr == 0:
                Row = CTkFrame(Frame,fg_color=fg)
                Row.pack(fill="x")
            if key == "current":
                continue
            
            cur = data[key]
            Block = CTkFrame(Row, fg_color=fg, width=200, height=100)
            Block.pack(side='left',padx=(0,20))
            change = Button(Block,command=lambda i=key,e=root: reload_fr(i,e,idt))
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
        global created,idt
        if created:
            return
        
        
        setts = Settings.Root()
        idt = setts
        setts.geometry("580x520")
        setts.config(background=fg)
        Head = LabelHead(setts)
        Head.configure(text="Settings")
        Head.pack()
        
        created = True
        frm = CTkScrollableFrame(setts,fg_color=fg)
        frm.pack(fill="both",expand=True)
        idt.protocol("WM_DELETE_WINDOW", Settings.close_settings)

        changer_frame = CTkFrame(frm,fg_color=fg)
        # changer_frame.pack(fill="both",expand=True)
        dropped[changer_frame] = 0

        db_change_frame = CTkFrame(frm,fg_color=fg)
        dropped[db_change_frame] = 0
    
        
        Settings.Pallet(changer_frame)
        Settings.set_database(db_change_frame)
        
        show = Button(frm)
        show.configure(command=lambda:Settings.drop_setts(changer_frame))
        show.pack()
        
        
        
        how = Button(frm)
        how.configure(command=lambda:Settings.drop_setts(db_change_frame))
        how.pack()

    def close_settings():
        global created
        created = False
        idt.destroy()

    def set_database(frm):
        Rad1 = CTkRadioButton(frm,fg_color=fg,text="Sql3",text_color=txt,)
        Rad1.pack()