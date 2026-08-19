from _Gui_.Pages import *
from _Gui_.ini_gui import *
from _Gui_.Buttons import Reload_butt


Place_Front_page()

def reloadwrap():
    Place_Front_page()
    Destroy_NJ_1page()

def startwrap():
    Remove_front_page()
    Place_NJ_1page()
    return

Reload_butt.pack()
Reload_butt.configure(command=lambda:reloadwrap())



start.configure(command=lambda:startwrap())






























root.mainloop()