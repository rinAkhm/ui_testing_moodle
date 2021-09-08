from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    PAGE_TO_AUTH = (By.XPATH, '//div[@class="usermenu"]/span/a')
    INPUT_USERNAME = (By.XPATH, '//div[@class="form-group"]/input[@type="text"]')
    INPUT_PASSWORD = (By.XPATH, '//div[@class="form-group"]/input[@type="password"]')
    BUTTON_LOGIN_ENTER = (By.ID, "loginbtn")
    FORM_PAGE = (By.ID, "page-wrapper")
    USER_BUTTON_IS_AUTH = (By.CLASS_NAME, "userbutton")
    BAR_USER_MENU = (By.CLASS_NAME, "usermenu")
    EXIT_USER_MENU = (By.ID, "actionmenuaction-6")
    ERROR_INPUT_AUTH = (By.ID, "loginerrormessage")
    CHEK_LOG_OUT = (By.XPATH, "//div[@class='forgetpass mt-3']/p")
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']")
