from Gui.GRoot import *

created = False

class Settings():

    def Create(master):
        global created
        if created:
            return
        setts = CTkToplevel(master)
        setts.geometry("580x520")
        setts.config(background=fg)
        created = True