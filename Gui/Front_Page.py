from utility.Wid_Snip import *
from Backend.Backpage_ import cur,rev
from Backend.Page_Wraper import wrappers

class FrontPage(CTkFrame):
    def __init__(self,master,app):
        super().__init__(
            master,
            fg_color=fg
        )
        self.widegets()
        self.app = app
    
    def widegets(self):
        self.StartLabel = LabelHead(self,text="Journal")


        self.Startbutt = Button(self)
        self.Startbutt.configure(text="Create New Journal")


        self.Startbutt.place(relx = 0.5,rely =0.4, relheight = 0.1, relwidth = 0.4,anchor="center")
        self.StartLabel.place(relx = 0.5,rely = 0.2, relheight = 0.4, relwidth = 0.6,anchor="center")

        self.Startbutt.configure(font=(Ft2,30),command=lambda:self.app.show_page("New_page1"))
        
    #* #############################################################
    
    def place_(self):
        self.place(relx = 0,rely =0, relheight = 1, relwidth = 1)
    
    def forget(self):
        self.place_forget()