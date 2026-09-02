from Gui.GRoot import *
from utility.Wid_Snip import *
from DBFile import *
from Backend.selection import selection,selected

buttsopen = {}
def plece(butt):                #Frame Open / Close Logic
    if buttsopen[butt] == 1:
        buttsopen[butt] = 0
        butt.pack_forget()
    elif buttsopen[butt] == 0:
        butt.pack(anchor='n')
        buttsopen[butt] = 1


Track_Sel = CTkScrollableFrame(root,fg_color=fg)

Row = CTkFrame(Track_Sel,fg_color=fg)
Row.pack(anchor='w')

catbutt = {}        #* Category Button
Dataframe = {}      #* Stores individual Checkbox inside types
catframe = {}       #* Stores the Frames for checkboxes

col = 3
for index,category in enumerate(journal_types.keys()):
    if index == 0:                  #* This block is fully row logic
        pass
    elif index % col == 0 :                   
        Row = CTkFrame(Track_Sel,fg_color=fg)
        Row.pack(anchor='w',pady=40)
        
    
    catframe[category] = CTkFrame(Row,fg_color=fg)                      #* Adds a frame to  "Frame storage for checkboxes"
    
    catbutt[category] = Button(Row)                                         #* Adds a button to Category buttons
    catbutt[category].configure(text=category,command=lambda i=catframe[category]:plece(i))      
    catbutt[category].pack(anchor="w",side="left",padx=40,pady=20)
    buttsopen[catframe[category]] = 0                                   #* Open / close logic


    Dataframe[category] = {}            #! Creates a Dict for current category
    for types in journal_types[category]:               #* to put selection button inside the catframe               
        Dataframe[category][types] = CTkCheckBox(catframe[category],text=types,fg_color=fg,hover_color=hv,font=(Ft2,20))
        Dataframe[category][types].pack(anchor="w")
        

        
def placethis():
    Track_Sel.pack(fill="both",anchor="nw",expand = True)