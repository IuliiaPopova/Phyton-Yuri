# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

from selenium.webdriver.support.select import Select

from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.init_new_contact_creation(wd)
        self.fill_contact_form(wd, Contact(firstname ="dfg", lastname = "fgdbf", address ="fghsfd", home_phone ="dfg", mobile_phone ="fgdbf",
                                           work_phone ="fghsfd", email ="dfg", email2 ="fgdbf", bday ="10", bmonth ="May",
                                           byear ="fgdbf", address2 ="fghsfd", phone2 ="fghsfd"))
        self.return_to_home_page(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.init_new_contact_creation(wd)
        self.fill_contact_form(wd, Contact(firstname ="", lastname ="", address ="", home_phone ="", mobile_phone ="",
                                           work_phone ="", email ="", email2 ="", bday ="-", bmonth ="-",
                                           byear ="", address2 ="", phone2 =""))
        self.return_to_home_page(wd)

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def fill_contact_form(self, wd, contact):
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("submit").click()

    def init_new_contact_creation(self, wd):
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbookv4.1.4/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()