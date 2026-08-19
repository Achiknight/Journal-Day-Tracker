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

JrName = CTkEntry(
                  text_color=txt,
                  fg_color=fg,
                  border_color=brd,
                  #border_width=2,
                  font=("Formula1 Display Regular", 50)
)




root.mainloop()