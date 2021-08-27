import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from models.auth import AuthData
from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--base-url")
    fixture = Application(webdriver.Chrome(ChromeDriverManager().install()), url)
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
