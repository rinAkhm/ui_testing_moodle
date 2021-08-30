import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from models.auth import AuthData
from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--base-url")
    chrome_options = Options()
    chrome_options.headless = True
    fixture = Application(
        webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options
        ),
        url,
    )
    yield fixture
    fixture.quit()


@pytest.fixture
def login_system(app, request):
    user = request.config.getoption("--login")
    password = request.config.getoption("--password")
    data = AuthData(login=user, password=password)
    app.login.auth(data)


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university",
        help="test_moodle_url",
    ),
    parser.addoption(
        "--login",
        action="store",
        default="rin_akhm@bk.ru",
        help="enter username",
    ),
    parser.addoption(
        "--password", action="store", default="Qwerty@321", help="enter password"
    ),
