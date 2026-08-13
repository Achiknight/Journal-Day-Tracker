from ini_gui import *
from Journal_py_.config import fg,hv,txt,brd




Head_label = CTkLabel(root,
                      font=('Runethia',40),
                      fg_color=fg,
                      text_color=txt,
                      text="Journal",
                      border_color=brd,
                      border_width=2)


start = CTkButton(root,
                  text="Click me",
                  fg_color=fg,
                  hover_color=hv,
                  border_color=brd,
                  border_width=2)










Head_label.pack()
start.pack()




root.mainloop()