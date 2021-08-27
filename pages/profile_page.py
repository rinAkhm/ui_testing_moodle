from locators.profile_page import ProfilePageLocators
from pages.base_page import BasePage
from common.constants import DataConstants
import random


class ProfilePage(BasePage):
    """Basic class for change profile data."""

    def open_profile(self):
        """Profile bar."""
        return self.find_element(ProfilePageLocators.PROFILE_MENU)

    def input_firstname(self):
        """First filed."""
        return self.find_element(ProfilePageLocators.FIRST_NAME)

    def input_lastname(self):
        """Lastname filed."""
        return self.find_element(ProfilePageLocators.LAST_NAME)

    def edit_profile(self):
        """Edit profile page."""
        return self.find_element(ProfilePageLocators.EDIT_PROFILE)

    def input_city(self):
        """filed city."""
        return self.find_element(ProfilePageLocators.CITY)

    def drop_down_country(self):
        """Drop down list."""
        return self.find_element(ProfilePageLocators.COUNTRY)

    def submit_save(self):
        """Button save."""
        return self.find_element(ProfilePageLocators.SAVE_PROFILE)

    def check_valid_changed(self):
        """Validation change."""
        text = self.find_element(ProfilePageLocators.CHECKING).text
        return text.strip()

    def choice_country(self):
        """Choice county form constants of list."""
        data = DataConstants()
        country = random.choice(data.country_list)
        return self.find_element(("xpath", f"//select/option[text()='{country}']"))

    def change_profile_data(self, name, lastname, city):
        """ "Edit profile."""
        self.click_element(self.user_menu())
        self.click_element(self.open_profile())
        self.click_element(self.edit_profile())
        self.fill_element(self.input_firstname(), name)
        self.fill_element(self.input_lastname(), lastname)
        self.fill_element(self.input_city(), city)
        self.click_element(self.drop_down_country())
        country = self.choice_country()
        self.click_element(country)
        self.click_element(self.submit_save())
