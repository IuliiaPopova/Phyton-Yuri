
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from fixture.contact import ContactHelper
from fixture.session2 import SessionHelper2

# Fixture
class Application2:

    def __init__(self):
        # Initialization of driver
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        # Link to fixture
        self.session2 = SessionHelper2(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbookv4.1.4/")


    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()