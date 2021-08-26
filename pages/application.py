from pages.login_page import LoginPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        # self.login_page = BasePage(self, driver, url)

    def open_main_page(self):
        self.driver.get(self.url + "/login/index.php")

    def quit(self):
        self.driver.quit()
