
from model.contact import Contact


# Test method takes as a parameter the fixture (app2)
def test_add_contact(app):
    app.session.login()
    app.contact.create(Contact(firstname ="dfg", lastname ="fgdbf", address ="fghsfd", home_phone ="dfg", mobile_phone ="fgdbf", work_phone ="fghsfd", email ="dfg", email2 ="fgdbf", bday ="10", bmonth ="May", byear ="fgdbf", address2 ="fghsfd", phone2 ="fghsfd"))

def test_add_empty_contact(app):
    app.session.login()
    app.contact.create(Contact(firstname ="", lastname ="", address ="", home_phone ="", mobile_phone ="", work_phone ="", email ="", email2 ="", bday ="-", bmonth ="-", byear ="", address2 ="", phone2 =""))
