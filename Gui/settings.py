from Gui.GRoot import *
from utility.Wid_Snip import *
from Backend.Pallet_Change import color_change,reload_widget_colors

created = False

class Settings():

    def Create(master):
        global created
        if created:
            return
        setts = CTkToplevel(master)
        setts.geometry("580x520")
        setts.config(background=fg)
        
        
        cenge = Button(root)
        cenge.configure(text="Change",command=lambda:color_change("vintage_editorial"))

        relo = Button(root)
        relo.configure(text="Reload",command=lambda:reload_widget_colors(root))
        created = True
