from Gui.GUI_Root import *
from utility.Wid_Snip import *
from DBFile import *
from Backend.selection import selection,selected
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


from customtkinter import *

 
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

        self.Row = CTkFrame(self,fg_color=fg)
        self.Row.pack(anchor='w')

        col = 3
        for index,category in enumerate(journal_types.keys()):
            if index == 0:                  #* This block is fully row logic
                pass
            elif index % col == 0 :                   
                self.Row = CTkFrame(self,fg_color=fg)
                self.Row.pack(anchor='w',pady=40)
                
            self.storage = CTkFrame(self.Row,fg_color=fg)                     #* Storage so that button and slection stack
            self.storage.pack(anchor="nw",pady=40,padx=20,side="left")
            
            self.catframe = CTkFrame(self.storage,fg_color=fg)                      #* Adds a frame for checkboxes"
            
            self.catbutt = Button(self.storage)                                         #* Adds a button to Category buttons
            self.catbutt.configure(text=category,command=lambda i=self.catframe:plece(i))      
            self.catbutt.pack(anchor="w",side="top",padx=40,pady=20)         #? Packed category buttons
            self.buttsopen[self.catframe] = 0                                   #* Open / close logic



            for types in self.journal_types[category]:               #* to put selection button inside the catframe               
                self.Dataframe = CTkCheckBox(self.catframe,text=types,fg_color=fg,text_color=txt,
                                                hover_color =hv,font=(Ft2,20),command=lambda tp=types:selection(selected,tp))
                self.Dataframe.pack(anchor="w")
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




