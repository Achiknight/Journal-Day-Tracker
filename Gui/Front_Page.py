from Gui.GRoot import *
from utility.Wid_Snip import *

StartLabel = CTkLabel(root,
    text="New Journal",
    text_color=txt,
    fg_color=fg,
    font=(Ft1, 130)
)

Startbutt = Button(root)
Startbutt.configure(text="Create New Journal")
Startbutt.configure(font=(Ft2,30))

def FrontPage():
    Startbutt.place(relx = 0.5,rely =0.4, relheight = 0.1, relwidth = 0.4,anchor="center")
    StartLabel.place(relx = 0.5,rely = 0.2, relheight = 0.4, relwidth = 0.6,anchor="center")

def FrontPageRemove():
    Startbutt.place_forget()
    StartLabel.place_forget()