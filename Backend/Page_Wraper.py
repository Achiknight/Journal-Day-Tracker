

class wrappers():
    def new_journal():
        from Gui.Front_Page import FrontPage
        from Gui.NameJournal import Place_NameJournal
        
        FrontPage.Forget()
        Place_NameJournal()
        
    def new_journal_selection():
        from Gui.NameJournal import Forget_NameJournal
        from Gui.Track_Selection import place_Track_sel
        
        Forget_NameJournal()
        place_Track_sel()

