from ..ini_gui import *


Front_frame = CTkFrame(root,
                       fg_color=fg,
                       )


Head_label = CTkLabel(Front_frame,
                      font=('Runethia',130),
                      fg_color=fg,
                      text_color=txt,
                      text="Journal",
                      #border_color=brd,
                      #border_width=2
                      )


start = CTkButton(Front_frame,
                  text="Click me",
                  text_color=txt,
                  fg_color=fg,
                  hover_color=hv,
                  border_color=brd,
                  border_width=2,
                  font=("Formula1 Display Regular",50)
                  )


def Place_Front_page():
    Front_frame.place(
        relx = 0,
        rely = 0,
        relwidth=1,
        relheight=1,
        #anchor="center"
        )
    Head_label.place(
        #x = 640,
        #y = 200,
        relx = 0.5,
        rely = 0.2,
        relwidth=0.5,
        relheight=0.4,
        anchor="center"
    )
    start.place(
        relx = 0.5,
        rely = 0.5,
        relwidth = 0.2,
        relheight = 0.1,
        anchor = "center"
    )
    return

def Remove_front_page():
    #Head_label.place_forget()
    #start.place_forget()
    Front_frame.place_forget()
    return




#Head_label.pack()
#start.pack()




#root.mainloop()