from Gui.GUI_Root import *

def Button(master, **kwargs):
    k = CTkButton(master,
                  text_color=txt,
                  fg_color=fg,
                  hover_color=hv,
                  border_color=brd,
                  border_width=2,
                  font=(Ft2, 50),
                  **kwargs)
    return k


def LabelHead(master, **kwargs):
    k = CTkLabel(master,
                 text_color=txt,
                 fg_color=fg,
                 font=(Ft1, 130),
                 **kwargs)
    return k


def LabelBody(master, **kwargs):
    k = CTkLabel(master,
                 text_color=txt,
                 fg_color=fg,
                 font=(Ft2, 30),
                 **kwargs)
    return k


def Entery(master, **kwargs):
    k = CTkEntry(master,
                 text_color=txt,
                 fg_color=fg,
                 border_color=brd,
                 border_width=2,
                 font=(Ft2, 30),
                 **kwargs)
    return k