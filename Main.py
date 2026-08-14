from Journal_py_._Gui_.Pages import *
from Journal_py_._Gui_.ini_gui import *
from Journal_py_._Gui_.Buttons import Reload_butt


Place_Front_page()

Reload_butt.pack()
Reload_butt.configure(command=lambda:Place_Front_page())

start.configure(command=lambda:Remove_front_page())






























root.mainloop()