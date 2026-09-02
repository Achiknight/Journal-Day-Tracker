from Gui.GRoot import *
from utility.Wid_Snip import *
from DBFile import *
from Backend.selection import selection,selected

buttsopen = {}
def plece(frm):                #Frame Open / Close Logic
    if buttsopen[frm] == 1:
        buttsopen[frm] = 0
        frm.pack_forget()
    elif buttsopen[frm] == 0:
        frm.pack(anchor='n',side="top")
        buttsopen[frm] = 1


Track_Sel = CTkScrollableFrame(root,fg_color=fg)

Row = CTkFrame(Track_Sel,fg_color=fg)
Row.pack(anchor='w')


col = 3
for index,category in enumerate(journal_types.keys()):
    if index == 0:                  #* This block is fully row logic
        pass
    elif index % col == 0 :                   
        Row = CTkFrame(Track_Sel,fg_color=fg)
        Row.pack(anchor='w',pady=40)
        
    storage = CTkFrame(Row,fg_color=fg)                     #* Storage so that button and slection stack
    storage.pack(anchor="nw",pady=40,padx=20,side="left")
    
    catframe = CTkFrame(storage,fg_color=fg)                      #* Adds a frame for checkboxes"
    
    catbutt = Button(storage)                                         #* Adds a button to Category buttons
    catbutt.configure(text=category,command=lambda i=catframe:plece(i))      
    catbutt.pack(anchor="w",side="top",padx=40,pady=20)
    buttsopen[catframe] = 0                                   #* Open / close logic



    for types in journal_types[category]:               #* to put selection button inside the catframe               
        Dataframe = CTkCheckBox(catframe,text=types,fg_color=fg,text_color=txt,
                                                 hover_color=hv,font=(Ft2,20),command=lambda tp=types:selection(tp))
        Dataframe.pack(anchor="w")
        
        
def placethis():
    Track_Sel.pack(fill="both",anchor="nw",expand = True)