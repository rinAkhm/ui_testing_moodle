from selenium.webdriver.common.by import By


class ProfilePageLocators:
    """Locators Profile page."""

    FIELD_PROFILE_MENU = (By.ID, "actionmenuaction-2")
    EDIT_PROFILE_LINK = (By.XPATH, "//li[@class = 'editprofile']/span/a")
    INPUT_FIRSTNAME = (By.ID, "id_firstname")
    INPUT_LASTNAME = (By.ID, "id_lastname")
    INPUT_CITY = (By.ID, "id_city")
    SELECT_COUNTRY = (By.ID, "id_country")
    BUTTON_SAVE_PROFILE = (By.ID, "id_submitbutton")
    TEXT_VALID_EDITING = (By.XPATH, "//span[@class='notifications']/div")
    BAR_USER_MENU = (By.CLASS_NAME, "usermenu")
    PROFILE_URL = (By.ID, "id_moodlenetprofile")
    SELECT_TIMEZONE = (By.ID, "id_timezone")
    SELECT_EMAIL_MOD = (By.ID, "id_maildisplay")
    TEXT_OPEN_PROFILE_PAGE = (
        By.XPATH,
        "//fieldset[@id='id_moodle']/legend/a[text()='Основные']",
    )
    ELEMENT_DOWNLOAD_IMAGE = (By.CLASS_NAME, "fp-btn-add")
    INPUT_IMAGE_FILE = (By.XPATH, "//div[@class='px-3']/input")
    BTN_UPLOAD_IMAGE_FILE = (By.XPATH, "//div[@class='mdl-align']/button")


class ErrorMassagePageLocators:
    ERROR_INPUT_FIRSTNAME = (By.ID, "id_error_firstname")
    ERROR_INPUT_LASTNAME = (By.ID, "id_error_lastname")
    ERROR = (By.ID, "id_moodle")
