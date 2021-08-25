import pytest
from pages.application import Application
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--base-url")
    app = Application(webdriver.Chrome(ChromeDriverManager().install()), url)
    yield app
    app.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university",
        help="test_moodle_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="rin_akhm@bk.ru",
        help="enter username",
    ),
    parser.addoption(
        "-password", action="store", defualt="Qwerty@321", help="enter password"
    )
