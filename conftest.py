import pytest
import logging
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from models.auth import AuthData
from pages.application import Application

logger = logging.getLogger("moodle")


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--base-url")
    Application.logger().info(f'Start browser = url is "{url}"')
    options = Options()
    options.add_argument("--start-maximized")
    options.headless = False
    fixture = Application(
        webdriver.Chrome(ChromeDriverManager().install(), options=options), url
    )
    yield fixture
    fixture.quit()


@pytest.fixture(scope="function")
def login_up(app, request):
    app.open_main_page()
    user = request.config.getoption("--login")
    password = request.config.getoption("--password")
    data = AuthData(login=user, password=password)
    app.login.auth(data)


@pytest.fixture(scope="session")
def get_auth_data(request):
    user = request.config.getoption("--login")
    password = request.config.getoption("--password")
    data = AuthData(login=user, password=password)
    return data


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
        "--password",
        action="store",
        default="Qwerty@321",
        help="enter password",
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            if "app" in item.fixturenames:
                web_driver = item.funcargs["app"]
            else:
                Application.logger().error("Fail to take screen-shot")
                return
            Application.logger().info("Screen-shot done")
            allure.attach(
                web_driver.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            Application.logger().error("Fail to take screen-shot: {}".format(e))
