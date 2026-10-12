from Gui.GUI_Root import *
from utility.Wid_Snip import *
from Backend.Backpage_ import cur,rev
from Backend.Page_Wraper import wrappers
 
class NewJournalP1(CTkFrame):
    def __init__(self,master,app):
        super().__init__(
            master,
            fg_color=fg
        )
        self.widgets()
        self.app = app
        
    def widgets(self):

        header = LabelHead(self,text="New Journal")

        Name = Entery(self)
        Name.configure(placeholder_text="Changes if already enterd once")
        Namelabel = LabelBody(self)
        Namelabel.configure(text="Your Name")

        JrName = Entery(self)
        JrNamelabel = LabelBody(self)
        JrNamelabel.configure(text="Journal Name")

        nextbtn = Button(self, text="To Selectables")
        nextbtn.configure(command=lambda: self.app.show_page("New_page2"))  #! Button CMD

        header.place(relx=0.5, rely=0.2, relheight=0.3, relwidth=0.6, anchor="center")

        Name.place(relx=0.6, rely=0.4, relheight=0.2, relwidth=0.41, anchor="center")
        Namelabel.place(relx=0.25, rely=0.4, relheight=0.1, relwidth=0.28, anchor="center")
        
        JrName.place(relx=0.6, rely=0.7, relheight=0.2, relwidth=0.4, anchor="center")
        JrNamelabel.place(relx=0.25, rely=0.7, relheight=0.2, relwidth=0.26, anchor="center")

        nextbtn.place(relx=0.5, rely=0.8, relheight=0.2, relwidth=0.26, anchor="center")
            
    def place_(self):
        print("NewJr p1 placed \n")
        self.place(relx = 0,rely =0, relheight = 1, relwidth = 1)
            
    def forget(self):
        self.place_forget()
        