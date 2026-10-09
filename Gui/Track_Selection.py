from Gui.GUI_Root import *
from utility.Wid_Snip import *
from DBFile import *

from Gui.settings import Settings
from Backend.Pallet_Change import color_change,reload_widget_colors

buttsopen = {}
def plece(frm):                #Frame Open / Close Logic
    if buttsopen[frm] == 1:
        buttsopen[frm] = 0
        frm.pack_forget()
    elif buttsopen[frm] == 0:
        frm.pack(anchor='n',side="top")
        buttsopen[frm] = 1
selected = []

def selection(selected,item):
    if item in selected:
        selected.remove(item)
    else:
        selected.append(item)
    print(selected)
    return

 
class NewJournalP2(CTkScrollableFrame):
    def ___init__(self,master):
        super().__init__(
            master,
            fg_color =fg            
        )
    def widgets(self):        
        self.head = LabelHead(self)
        self.head.configure(text="Select Trackables")
        self.head.pack()

        Row = CTkFrame(self,fg_color=fg)
        Row.pack(anchor='w')

        col = 3
        for index,category in enumerate(journal_types.keys()):
            if index == 0:                  #* This block is fully row logic
                pass
            elif index % col == 0 :                   
                Row = CTkFrame(self,fg_color=fg)
                Row.pack(anchor='w',pady=40)
                
            storage = CTkFrame(Row,fg_color=fg)                     #* Storage so that button and slection stack
            storage.pack(anchor="nw",pady=40,padx=20,side="left")
            
            catframe = CTkFrame(storage,fg_color=fg)                      #* Adds a frame for checkboxes"
            
            catbutt = Button(storage)                                         #* Adds a button to Category buttons
            catbutt.configure(text=category,command=lambda i=catframe:plece(i))      
            catbutt.pack(anchor="w",side="top",padx=40,pady=20)         #? Packed category buttons
            buttsopen[catframe] = 0                                   #* Open / close logic



            for types in self.journal_types[category]:               #* to put selection button inside the catframe               
                Dataframe = CTkCheckBox(catframe,text=types,fg_color=fg,text_color=txt,
                                                hover_color =hv,font=(Ft2,20),command=lambda tp=types:selection(selected,tp))
                Dataframe.pack(anchor="w")
                
                
        def Place(self):
            self.place(relx = 0,rely = 0, relheight = 1, relwidth = 1)

        def Forget(self):
            self.place_forget()


# #! Testing purpose button
# set = Button(Track_Sel)
# set.configure(command=lambda:Settings.Create(root))
# set.pack()

# placeholder = Button(Track_Sel)
# placeholder.configure(command=lambda:Settings.Create(root))




