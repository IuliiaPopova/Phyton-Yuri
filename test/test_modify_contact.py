from model.contact import Contact


# Test method takes as a parameter the fixture (app2)
def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname ="New firstname"))


def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname ="New lastname"))
