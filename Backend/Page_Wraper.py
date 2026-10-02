

class wrappers():
    def new_journal():
        from Gui.Front_Page import Forget_FrontPage
        from Gui.NameJournal import Place_NameJournal
        
        Forget_FrontPage()
        Place_NameJournal()
        
    def new_journal_selection():
        from Gui.NameJournal import Forget_NameJournal
        from Gui.Track_Selection import place_Track_sel
        
        Forget_NameJournal()
        place_Track_sel()

