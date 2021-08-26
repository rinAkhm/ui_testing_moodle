import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--base-url")
    fixture = Application(webdriver.Chrome(ChromeDriverManager().install()), url)
    yield fixture
    fixture.quit()


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
        "--password", action="store", default="Qwerty@321", help="enter password"
    ),
