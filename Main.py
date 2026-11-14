from customtkinter import *
from Gui import *   

app = MainWindow()

start = FrontPage(app.root, app)
start.place_()
app.add_page("Front_page",start)


name = NewJournalP1(app.root,app)
select = NewJournalP2(app.root,app)
write = EntryPage(app.root,app)
load = LoadJournal(app.root,app)

app.add_page("New_page1",name)
app.add_page("New_page2",select)
app.add_page("entry_page",write)
app.add_page("load_page",load)

app.setup_protocol()
app.update()