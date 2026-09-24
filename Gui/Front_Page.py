from Gui.GRoot import root
from utility.Wid_Snip import *
from Backend.Backpage_ import cur,rev
from Gui.NameJournal import Place_NameJournal
from Backend.Page_Wraper import wrappers


frame = CTkFrame(root,fg_color=fg)


StartLabel = LabelHead(frame,text="Journal")


Startbutt = Button(frame)
Startbutt.configure(text="Create New Journal")


Startbutt.place(relx = 0.5,rely =0.4, relheight = 0.1, relwidth = 0.4,anchor="center")
StartLabel.place(relx = 0.5,rely = 0.2, relheight = 0.4, relwidth = 0.6,anchor="center")

def Place_FrontPage():
    global cur,rev
    frame.place(relx = 0,rely =0, relheight = 1, relwidth = 1)


def Forget_FrontPage():
    global cur,rev
    frame.place_forget()

Startbutt.configure(font=(Ft2,30),command=lambda:wrappers.new_journal())