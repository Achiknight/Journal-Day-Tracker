from Gui.GRoot import *
from utility.Wid_Snip import *
from DBFile import *
from Backend.selection import selection,selected

def plece(ame):
    ame.pack()


Track_Sel = CTkScrollableFrame(root,fg_color=fg)

Row = CTkFrame(Track_Sel,fg_color=fg)
Row.pack(anchor='w')

catbutt = {}
Dataframe = {}


col = 3
for index,category in enumerate(journal_types.keys()):
    if index == 0:
        pass
    elif col % index == 0 :
        Row = CTkFrame(Track_Sel,fg_color=fg)
        Row.pack(anchor='w')
    NewF = CTkFrame(Row,fg_color=fg)
    catbutt[category] = Button(Row)
    catbutt[category].configure(text=category,command=lambda:plece(NewF))
    catbutt[category].pack(anchor="w",side="left")

    Dataframe[category] = {}
    for types in category:
        Dataframe[category][types] = CTkCheckBox(NewF,text=types,fg_color=fg,hover_color=hv,font=(Ft2,20))
        Dataframe[category][types].pack(anchor="w")
        
        
        
        
def placethis():
    Track_Sel.pack(fill="both")