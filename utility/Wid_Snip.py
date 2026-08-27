from Gui.GRoot import *

def Button(master):
    k = CTkButton(master,
                  text="Click me",
                  text_color=txt,
                  fg_color=fg,
                  hover_color=hv,
                  border_color=brd,
                  border_width=2,
                  font=(Ft2, 50))
    return k

def LabelHead(master):
    k = CTkLabel(master,
                 text="Click me",
                 text_color=txt,
                 fg_color=fg,
                 font=(Ft1, 130))
    return k

def LabelBody(master):
    k = CTkLabel(master,
                 text="Click me",
                 text_color=txt,
                 fg_color=fg,
                 font=(Ft2, 30))
    return k 

def Entery(master):
    k = CTkEntry(master,
                 text_color=txt,
                 fg_color=fg,
                 border_color=brd,
                 border_width=2,
                 font=(Ft2, 30))
    return k