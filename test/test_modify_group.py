

from model.group import Group

def test_modify_group_name(app):
    app.session.login()
    app.group.modify_first_group(Group(name ="New name"))


def test_modify_group_header(app):
    app.session.login()
    app.group.modify_first_group(Group(header ="New header"))