
from model.group import Group

def test_add_group(app):
    app.session.login()
    app.group.create(Group(name ="dfg", header ="fgdbf", footer ="fghsfd"))

def test_add_empty_group(app):
    app.session.login()
    app.group.create(Group(name ="", header ="", footer =""))
