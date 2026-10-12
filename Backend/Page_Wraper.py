from Gui import *

class wrappers():
    def new_journal():

        
        FrontPage.forget()
        NewJournalP1.place()
        
    def new_journal_selection():
        from Gui.NameJournal import Forget_NameJournal
        from Gui.Track_Selection import place_Track_sel
        
        Forget_NameJournal()
        place_Track_sel()

