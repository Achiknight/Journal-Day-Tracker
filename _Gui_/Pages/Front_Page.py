from ..ini_gui import *





Head_label = CTkLabel(root,
                      font=('Runethia',130),
                      fg_color=fg,
                      text_color=txt,
                      text="Journal",
                      #border_color=brd,
                      #border_width=2
                      )


start = CTkButton(root,
                  text="Click me",
                  text_color=txt,
                  fg_color=fg,
                  hover_color=hv,
                  border_color=brd,
                  border_width=2
                  )


def Place_Front_page():
    Head_label.place(
        relx = 0.46,
        rely = 0.2,
        relwidth=0.5,
        relheight=0.4,
        anchor="center"
    )
    return




Place_Front_page()


#Head_label.pack()
#start.pack()




root.mainloop()