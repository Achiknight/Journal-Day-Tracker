from customtkinter import *
from utility.Wid_Snip import *
from Gui.widgets import Journal_Widgets




class EntryPage(CTkScrollableFrame):
    def __init__(self,master,app):
            self.class_entry = {}
            super().__init__(
                master,
                fg_color=fg
                
            )
            self.app = app
            
    def widgets(self, selection :list):
        for index,function in enumerate(selection):
            if index % 2 == 0:
                Row = CTkFrame(self,fg_color=fg)
                Row.pack()
            
            rowbox = CTkFrame(self,fg_color=fg)
            rowbox.pack(side="left",pady=40,padx=20,anchor="nw")
            
            k = Journal_Widgets.FIELD_BUILDERS[function](rowbox)
            
            self.class_entry[function] = k
        
        next_button = Button(self,text="Next",command=NONE)
    
    def place_(self):
        self.place(relx = 0,rely =0, relheight = 1, relwidth = 1)
        
    def forget(self):
        self.place_forget()
        