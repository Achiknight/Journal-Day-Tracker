from Gui.GRoot import *
from utility.Wid_Snip import *


NameJournal = CTkFrame(root,fg_color=fg)

header = LabelHead(NameJournal)
header.configure(text="New Journal")

Name = Entery(NameJournal)
Name.configure(placeholder_text="Changes if already enterd once")
Namelabel = LabelBody(NameJournal)
Namelabel.configure(text="Your Name")

JrName = Entery(NameJournal)
JrNamelabel = LabelBody(NameJournal)
JrNamelabel.configure(text="Journal Name")

def PlaceNJ():
    NameJournal.place(relx = 0,rely =0, relheight = 1, relwidth = 1)
    header.place(relx = 0.5,rely =0.2, relheight = 0.3, relwidth = 0.6,anchor="center")
    
    Name.place(relx = 0.6,rely =0.4, relheight = 0.2, relwidth = 0.41,anchor="center")
    Namelabel.place(relx = 0.25 , rely = 0.4 , relheight = 0.1, relwidth = 0.28,anchor="center")
    
    JrName.place(relx = 0.6,rely = 0.7, relheight = 0.2, relwidth = 0.4,anchor="center")
    JrNamelabel.place(relx = 0.25,rely = 0.7, relheight = 0.2, relwidth = 0.26,anchor="center")