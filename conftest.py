
import pytest

from fixture.application import Application

# Fixrure is created only once for the whole session
@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    # Destroy of fixture
    request.addfinalizer(fixture.destroy)
    return fixture