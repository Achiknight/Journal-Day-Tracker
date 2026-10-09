from customtkinter import *
from Gui import *

app = MainWindow()
print("Root created")

start = FrontPage(app.root)
print("FrontPage created:", start.winfo_exists())

start.Place()
print("FrontPage placed:", start.winfo_manager())



# app.setup_protocol()
app.update()