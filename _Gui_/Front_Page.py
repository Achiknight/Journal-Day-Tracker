from .ini_gui import *





Head_label = CTkLabel(root,
                      font=('Runethia',120),
                      fg_color=fg,
                      text_color=txt,
                      text="Journal",
                      border_color=brd,
                      border_width=2)


start = CTkButton(root,
                  text="Click me",
                  text_color=txt,
                  fg_color=fg,
                  hover_color=hv,
                  border_color=brd,
                  border_width=2)










Head_label.pack()
start.pack()




root.mainloop()