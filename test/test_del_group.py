

def test_delite_first_group(app):
    app.session.login()
    app.group.delite_first_group()
