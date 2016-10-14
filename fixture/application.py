
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.session import SessionHelper


class Application:
    # Constructor
    def __init__(self):
        # Initialization driver
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def is_valid(self):
        # if
        try:
            # browser should determine the current address of the web page
            self.wd.current_url
            return True
        # else
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbookv4.1.4/")


    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    # Destroy fixture
    def destroy(self):
        self.wd.quit()