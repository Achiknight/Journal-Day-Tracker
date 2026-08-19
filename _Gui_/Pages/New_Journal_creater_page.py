from ..ini_gui import *

Journal_t_n = ''

NewJournal = CTkFrame(root,fg_color=fg)

Title = CTkLabel(NewJournal,
                fg_color=fg,
                text_color=txt,
                border_color=brd,
                text="New Journal",
                font=('Runethia',130)
                )

JrName = CTkEntry(NewJournal,
                  text_color=txt,
                  fg_color=fg,
                  border_color=brd,
                  #border_width=2,
                  font=("Formula1 Display Regular", 50)
)

def Place_NJ_1page():
    NewJournal.place(relx = 0,rely = 0, relheight = 1,relwidth = 1)
    Title.place(relx = 0.5,rely = 0.2, relheight = 0.4, relwidth = 0.6,anchor="center")
    JrName.place(relx = 0.5 ,rely = 0.4, relheight = 0.1, relwidth = 0.6,anchor="center")
    return
def Destroy_NJ_1page():
    NewJournal.place_forget()



