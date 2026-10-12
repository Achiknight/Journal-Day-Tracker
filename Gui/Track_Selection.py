from customtkinter import *
from utility.Wid_Snip import Entery,LabelBody,LabelHead,Button
from DBFile.JR_types import journal_types
from Backend.config import fg,txt,Ft1,Ft2,brd,hv
from Gui.entry_page import EntryPage

 
class NewJournalP2(CTkScrollableFrame):
   
    def __init__(self,master,app):
        super().__init__(
            master,
            fg_color=fg            
        )
        self.app = app
        self.buttsopen = {}
        self.selected = []
        self.widgets()
    
    
    def plece(self,frm):      #Frame Open / Close Logic
        if self.buttsopen[frm] == 1:
            self.buttsopen[frm] = 0
            frm.pack_forget()
        elif self.buttsopen[frm] == 0:
            frm.pack(anchor='n',side="top")
            self.buttsopen[frm] = 1
            return

    def selection(self,selected,item):
        if item in selected:
            selected.remove(item)
        else:
            selected.append(item)
        print(selected)
        return

        
        
    def widgets(self):        
        head = LabelHead(self)
        head.configure(text="Select Trackables")
        head.pack()

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
            catbutt.configure(text=category,command=lambda i=catframe:self.plece(i))      
            catbutt.pack(anchor="w",side="top",padx=40,pady=20)         #? Packed category buttons
            self.buttsopen[catframe] = 0                                   #* Open / close logic



            for types in journal_types[category]:               #* to put selection button inside the catframe               
                Dataframe = CTkCheckBox(catframe,text=types,fg_color=fg,text_color=txt,
                                                hover_color =hv,font=(Ft2,20),command=lambda tp=types:self.selection(self.selected,tp))
                Dataframe.pack(anchor="w")
            
        nextbutton = Button(self,text = "Next",command=lambda:self.wrapper())
        nextbutton.pack()
                
    def place_(self):
            self.place(relx = 0,rely = 0, relheight = 1, relwidth = 1)

    def forget(self):
            self.place_forget()

    def wrapper(self):
        EntryPage.widgets(EntryPage,self.selected)
        self.app.show_page("entry_page")




























# #! Testing purpose button
# set = Button(Track_Sel)
# set.configure(command=lambda:Settings.Create(root))
# set.pack()

# placeholder = Button(Track_Sel)
# placeholder.configure(command=lambda:Settings.Create(root))




