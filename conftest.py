
import pytest

from fixture.application import Application


fixture = None


# Fixrure is created only once for the whole session
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login()
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login()

    # fixture.session.login(username = "admin", password = "secret")
    def fin():
        # fixture.session.logout()
        # Destroy of fixture
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture