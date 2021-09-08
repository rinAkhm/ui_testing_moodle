import logging

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.profile = ProfilePage(self)

    def open_main_page(self):
        self.driver.get(self.url + "/login/index.php")

    def quit(self):
        self.driver.quit()

    def make_screenshot(self):
        return self.driver.get_screenshot_as_png()

    @staticmethod
    def logger():
        return logging.getLogger("moodle")
