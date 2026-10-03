from customtkinter import *
from Backend.config import fg,txt,Ft1,Ft2,brd,hv

class MainWindow():
    def __init__(self):
        self.root = CTk()
        self.root.geometry("1280x720")
        self.root.config(background=fg)
        
    def Update(self):
        self.root.mainloop
        
    def Destroy(self):
        self.root.protocol("WM_DELETE_WINDOW", MainWindow.Close)
    
    def Close(self):
        self.root.destroy()