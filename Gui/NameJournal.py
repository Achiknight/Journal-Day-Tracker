from Gui.GUI_Root import *
from utility.Wid_Snip import *
from Backend.Backpage_ import cur,rev
from Backend.Page_Wraper import wrappers
 
class NewJournalP1(CTkFrame):
    def __init__(self,master):
        super().__init__(
            master,
            fg_color=fg
        )
    
    def widgets(self):
        self.header = LabelHead(self)
        self.header.configure(text="New Journal")

        self.Name = Entery(self)
        self.Name.configure(placeholder_text="Changes if already enterd once")
        self.Namelabel = LabelBody(self)
        self.Namelabel.configure(text="Your Name")

        self.JrName = Entery(self)
        self.JrNamelabel = LabelBody(self)
        self.JrNamelabel.configure(text="Journal Name")
        
        
        self.header.place(relx = 0.5,rely =0.2, relheight = 0.3, relwidth = 0.6,anchor="center")

        self.Name.place(relx = 0.6,rely =0.4, relheight = 0.2, relwidth = 0.41,anchor="center")
        self.Namelabel.place(relx = 0.25 , rely = 0.4 , relheight = 0.1, relwidth = 0.28,anchor="center")

        self.JrName.place(relx = 0.6, rely = 0.7, relheight = 0.2, relwidth = 0.4,anchor="center")
        self.JrNamelabel.place(relx = 0.25,rely = 0.7, relheight = 0.2, relwidth = 0.26,anchor="center")
        
        
           
    def Place(self):
        self.place(relx = 0,rely =0, relheight = 1, relwidth = 1)
            
    def Forget(self):
        self.place_forget()
        