
class SessionHelper2:

    # Constructor
    def __init__(self, app2):
        self.app2 = app2


    def login (self):
        wd = self.app2.wd
        self.app2.open_home_page()