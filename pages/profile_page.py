import time

from locators.profile_page import ProfilePageLocators, ErrorMassagePageLocators
from selenium.webdriver.remote.webelement import WebElement
from models.profile import ProfileData

from pages.base_page import BasePage


class ProfilePage(BasePage):
    """Basic class for change profile data."""

    def open_profile(self) -> WebElement:
        """Profile bar."""
        return self.find_element(ProfilePageLocators.FIELD_PROFILE_MENU)

    def input_firstname(self) -> WebElement:
        """First filed."""
        return self.find_element(ProfilePageLocators.INPUT_FIRSTNAME)

    def input_lastname(self) -> WebElement:
        """Lastname filed."""
        return self.find_element(ProfilePageLocators.INPUT_LASTNAME)

    def edit_profile(self) -> WebElement:
        """Edit profile page."""
        return self.find_element(ProfilePageLocators.EDIT_PROFILE_LINK)

    def input_city(self) -> WebElement:
        """filed city."""
        return self.find_element(ProfilePageLocators.INPUT_CITY)

    def input_url_profile(self) -> WebElement:
        """Filed MoodleNet."""
        return self.find_element(ProfilePageLocators.PROFILE_URL)

    def choice_timezone(self) -> WebElement:
        """Dropdown timezone."""
        return self.find_element(ProfilePageLocators.SELECT_TIMEZONE)

    def submit_save(self) -> WebElement:
        """Button save."""
        return self.find_clickable_element(ProfilePageLocators.BUTTON_SAVE_PROFILE)

    def check_valid_changed(self) -> str:
        """Validation change."""
        text = self.find_element(ProfilePageLocators.TEXT_VALID_EDITING).text
        return text.strip()

    def user_menu(self) -> WebElement:
        """Board with user menu."""
        return self.find_element(ProfilePageLocators.BAR_USER_MENU)

    def open_profile_changed(self) -> None:
        """Profile page."""
        self.click_element(self.user_menu())
        self.click_element(self.open_profile())
        self.click_element(self.edit_profile())

    def select_country(self, county: str) -> WebElement:
        """Choice county."""
        return self.select_value(
            self.select_element(ProfilePageLocators.SELECT_COUNTRY), county
        )

    def select_email_mod(self, email_mod: str) -> WebElement:
        """Choice email mod."""
        return self.select_value(
            self.select_element(ProfilePageLocators.SELECT_EMAIL_MOD), email_mod
        )

    def select_timezone(self, timezone: str) -> WebElement:
        """Choice timezone."""
        return self.select_value(
            self.select_element(ProfilePageLocators.SELECT_TIMEZONE), timezone
        )

    def is_open_changed_page(self) -> bool:
        """Profile is page."""
        element = self.find_elements(ProfilePageLocators.TEXT_OPEN_PROFILE_PAGE)
        if len(element) > 0:
            return True
        return False

    def image_file_download(self):
        """Click element file for download image."""
        return self.find_clickable_element(ProfilePageLocators.ELEMENT_DOWNLOAD_IMAGE)

    def input_file_image(self):
        """Send image file element."""
        return self.find_clickable_element(ProfilePageLocators.INPUT_IMAGE_FILE)

    def upload_image_file(self):
        """Upload image file."""
        return self.find_clickable_element(ProfilePageLocators.BTN_UPLOAD_IMAGE_FILE)

    def input_image(self, path):
        """Set image profile."""
        self.click_element(self.image_file_download())
        time.sleep(2)
        self.fill_element(self.input_file_image(), path)
        time.sleep(2)
        self.click_element(self.upload_image_file())
        time.sleep(2)

    def change_profile_data(self, data: ProfileData) -> None:
        """Input data."""
        if not self.is_open_changed_page():
            self.open_profile_changed()
            self.app.logger().info("Profile page opened successfully")
        self.app.logger().info(
            f"data for editing profile:\n"
            f'name-"{data.firstname}" surname-"{data.lastname}"\n'
            f'city-"{data.city}" url-"{data.moodle_net}"\n'
            f'country-"{data.country}" timezone-"{data.timezone}"\n'
            f'path to image_file-"{data.image}"'
        )
        self.fill_element(self.input_firstname(), data.firstname)
        self.fill_element(self.input_lastname(), data.lastname)
        self.fill_element(self.input_city(), data.city)
        self.fill_element(self.input_url_profile(), data.moodle_net)
        self.select_email_mod(data.email_mod)
        self.select_country(data.country)
        self.select_timezone(data.timezone)
        self.input_image(data.image)
        self.click_element(self.submit_save())

    def error_input_firstname(self):
        return self.find_element(ErrorMassagePageLocators.ERROR_INPUT_FIRSTNAME).text

    def error_input_lastname(self):
        return self.find_element(ErrorMassagePageLocators.ERROR_INPUT_LASTNAME).text

    def check_required_fields(self, data):
        if not self.is_open_changed_page():
            self.open_profile_changed()
            self.app.logger().info("Profile page opened successfully")
        self.app.logger().info(
            f"data for editing profile:\n"
            f'name-"{data.firstname}" surname-"{data.lastname}"'
        )
        self.fill_element(self.input_firstname(), data.firstname)
        self.fill_element(self.input_lastname(), data.lastname)
        if data.firstname is None:
            element = self.error_input_firstname()
            self.click_element(self.submit_save())
            return element
        element = self.error_input_lastname()
        self.click_element(self.submit_save())
        return element
