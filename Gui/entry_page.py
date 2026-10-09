from customtkinter import *
from utility.Wid_Snip import *
from Gui.widgets import Journal_Widgets

class_entry = {}


class EntryPage(CTkScrollableFrame):
    def __init__(self,master):
            super().__init__(
                master,
                fg_color=fg
            )
            
    def widgets(self, selection :list):
        for index,function in enumerate(selection):
            if index % 2 == 0:
                Row = CTkFrame(self,fg_color=fg)
                Row.pack()
            
            rowbox = CTkFrame(self,fg_color=fg)
            rowbox.pack(side="left",pady=40,padx=20,anchor="nw")
            
            k = Journal_Widgets.FIELD_BUILDERS[function](rowbox)
            
            class_entry[function] = k