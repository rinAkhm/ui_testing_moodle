# from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, app):
        self.app = app

    def auth(self, login: str, password: str):
        return self.drive.get(self.url)
