from customtkinter import *
from Backend.config import fg,txt,Ft1,Ft2,brd,hv

class MainWindow():
    def __init__(self):
        self.root = CTk()
        self.root.geometry("1280x720")
        self.root.config(background=fg)
        self.pages = {}
        
            
    def add_page(self, name : str, page):
        print(f"added {name}")
        self.pages[name] = page

    def show_page(self, name):
        print(self.pages)
        for page in self.pages.values():
            page.forget()

        self.pages[name].place_()
    
    
    def update(self):
        self.root.mainloop()
        
    def setup_protocol(self):
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def close(self):
        self.root.destroy()