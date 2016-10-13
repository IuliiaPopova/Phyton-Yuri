
# Test method takes as a parameter the fixture (app)
def test_delete_first_contact(app):
    app.contact.delete_first_contact()
