from selenium.webdriver.common.by import By


class ProfilePageLocators:
    """Locators Profile page."""

    PROFILE_MENU = (By.ID, "actionmenuaction-2")
    EDIT_PROFILE = (By.XPATH, "//li[@class = 'editprofile']/span/a")
    FIRST_NAME = (By.ID, "id_firstname")
    LAST_NAME = (By.ID, "id_lastname")
    CITY = (By.ID, "id_city")
    COUNTRY = (By.ID, "id_country")
    SAVE_PROFILE = (By.ID, "id_submitbutton")
    CHECKING = (By.XPATH, "//span[@class='notifications']/div")
