from login_page import LoginPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.main_page = LoginPage(self)

    def quit(self):
        self.driver.quit()
