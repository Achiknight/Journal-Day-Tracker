from customtkinter import *
from Backend.config import fg,txt,Ft1,Ft2,brd,hv

class MainWindow():
    def __init__(self):
        self.root = CTk()
        self.root.geometry("1280x720")
        self.root.config(background=fg)
        
        
    def update(self):
        self.root.mainloop()
        
    def setup_protocol(self):
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def close(self):
        self.root.destroy()