import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    admin_pass = request.config.getoption("--adminsPass")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url, admin_pass=admin_pass)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url, admin_pass=admin_pass)
    fixture.session.ensure_login(username="admin", password=admin_pass)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseUrl", action="store", default="http://10.50.26.174/addressbook/")
    parser.addoption("--adminsPass", action="store", default="")
