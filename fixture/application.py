
from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper

class Application:

    # Constructor
    def __init__(self):
        #Initialization driver
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbookv4.1.4/")

    # Destroy fixture
    def destroy(self):
        self.wd.quit()