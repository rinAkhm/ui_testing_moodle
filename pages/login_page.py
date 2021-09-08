from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from locators.login_page import AuthorizationPageLocators


class LoginPage(BasePage):
    """Moodle login page."""

    def is_auth(self) -> bool:
        """Check to auth in moodle."""
        self.find_element(AuthorizationPageLocators.FORM_PAGE)
        element_auth = self.find_elements(AuthorizationPageLocators.USER_BUTTON_IS_AUTH)
        if len(element_auth) > 0:
            return True
        return False

    def input_username(self) -> WebElement:
        """Input username to filed of form."""
        return self.find_element(AuthorizationPageLocators.INPUT_USERNAME)

    def input_password(self) -> WebElement:
        """Input password to filed of form."""
        return self.find_element(AuthorizationPageLocators.INPUT_PASSWORD)

    def open_auth_page(self) -> WebElement:
        """Open page authorization."""
        return self.find_element(AuthorizationPageLocators.PAGE_TO_AUTH)

    def submit_auth_form(self) -> WebElement:
        """Button submit."""
        return self.find_element(AuthorizationPageLocators.BUTTON_LOGIN_ENTER)

    def user_menu(self) -> WebElement:
        """Cell is user menu."""
        return self.find_element(AuthorizationPageLocators.BAR_USER_MENU)

    def exit_system(self) -> WebElement:
        """Field for sign out."""
        return self.find_element(AuthorizationPageLocators.EXIT_USER_MENU)

    def login_error(self):
        """Search massage that login error."""
        return self.find_element(AuthorizationPageLocators.ERROR_INPUT_AUTH).text

    def check_log_out(self):
        """Search text for log out."""
        return self.find_element(AuthorizationPageLocators.CHEK_LOG_OUT).text

    def find_exit_button(self):
        """Permission to log out of the system."""
        return self.find_elements(AuthorizationPageLocators.BUTTON_EXIT)

    def auth(self, data) -> None:
        """Process authorization in moodle."""
        if self.find_exit_button():
            self.click_element(self.find_exit_button()[0])
        if self.is_auth():
            self.app.logger().info("checking that you are logged in")
            self.click_element(self.user_menu())
            self.click_element(self.exit_system())
        self.app.logger().info(
            f'Sign in system with login - "{data.login}" '
            f'password - "{data.password}"'
        )
        self.fill_element(self.input_username(), data.login)
        self.fill_element(self.input_password(), data.password)
        self.click_element(self.submit_auth_form())
