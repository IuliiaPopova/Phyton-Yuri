
class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self):
        #wd = self.app.wd
        self.app.open_home_page()


    #def login(self, username, password):
        #wd = self.app.wd
        #wd.find_element_by_page("user").click()
        #wd.find_element_by_page("user").clear()
        #wd.find_element_by_page("user").send_keys(username)
        #wd.find_element_by_page("pass").click()
        #wd.find_element_by_page("pass").clear()
        #wd.find_element_by_page("pass").send_keys(password)
        #wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    #def logout(self):
        #wd = self.app.wd
        #wd.find_element_by_link_text("Logout").click()

    #def ensure_logout(self):
        #wd = self.app.wd
        # if we inside active session and we have element "Logout" on the page, then we must to click on "Logout"
        # we need to calculate the number of elements "Logout" on the page
        #if len(wd.find_elements_by_link_text("Logout")) > 0:
        #    self.logout()

    #def ensure_login(self, username, password):
        wd = self.app.wd

