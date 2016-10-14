
import pytest

from fixture.application import Application

# Global variable
# Fixture is not defined
fixture = None

# Fixture is created only once for the whole session
@pytest.fixture
def app(request):
    # we use a global variable
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login()
        # fixture.session.login(username = "admin", password = "secret")
    else:
        # if fuxture is not working properly
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login()
            # fixture.session.login(username = "admin", password = "secret")
    return fixture

# Finalization happens once at the end
# autouse = True - fixture use automatically
@pytest.fixture (scope = "session", autouse = True)
def stop(request):
    def fin():
        # fixture.session.logout()
        # Destroy of fixture
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture