from customtkinter import *
from utility.Wid_Snip import *
from Backend.sql_functions import fetch_tables
from DBFile.Connection import cur,data

class LoadJournal(CTkScrollableFrame):
    def __init__(self,master :any,app):
        super().__init__(
            master,
            fg_color=fg
        )
        self.app = app
        self.widgets()
        
        
    
    def widgets(self):

        for tables in (fetch_tables(cur,data)):
            k = Button(self,command = lambda e = tables :self.name(e))
            k.configure(text=tables)
            k.pack(padx=50,pady=10,anchor="nw")
            
    def name(self,table):
        self.app.name = table
        
    def place_(self):
        self.place(relx = 0,rely =0, relheight = 1, relwidth = 1)
        
    def forget(self):
        self.place_forget()