from selenium.webdriver.support.select import Select


class ContactHelper:

    # Constructor
    def __init__(self, app):
        self.app = app


    def init_new_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.init_new_contact_creation()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.app.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value_select("bday", contact.bday)
        self.change_field_value_select("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)

    def change_field_value_select(self, field_name, text):
        wd = self.app.wd

        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        # meniautca tolko znacheniya v poliah vvoda, kotoree mi zadaem
        # esli mi ne upominaem eto pole vvoda, to ect ono = None, to tam nichego ne menaetsa
        # mi meniaem tolko te svoestva obekta, kototie nas interesuyut
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # Delete
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_xpath("(//input[@name='update'])[1]").click()
        self.app.return_to_home_page()


    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()
