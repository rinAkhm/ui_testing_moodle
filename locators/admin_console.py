from selenium.webdriver.common.by import By


class BarLocators:
    BTN_ADMIN_BAR = (By.XPATH, "//a[@data-key='sitesettings']")
    ADMIN_PAGE = (By.XPATH, "//div[@class='alert-error']/h2")


class AdminInterfaceLocators:
    LINK_COURSES = (By.XPATH, "//a[@href='#linkcourses']")
    LINK_MANAGER_COURSE = (
        By.XPATH,
        "//a[@href='https://qacoursemoodle.innopolis."
        "university/course/management.php']",
    )
    LINK_ADD_COURSE = (
        By.XPATH,
        "//a[@href='https://qacoursemoodle."
        "innopolis.university/course/edit.php?category=0']",
    )
    FULL_NAME_COURSE = (By.XPATH, "//div[@id='fitem_id_fullname']/div[2]/input")
    SHORT_NAME_COURSE = (By.XPATH, "//div[@id='fitem_id_shortname']/div[2]/input")
    BTN_SAVE = (By.ID, "id_saveanddisplay")
    CHECK_NEW_COURSE = (By.CLASS_NAME, "page-header-headings")
    ICON_DELETE_COURSE = (By.CLASS_NAME, "action-delete")
    BTN_DELETE = (By.XPATH, "//button[@type='submit']")
    MESSAGE_DELETE = (By.XPATH, "//h2[2]")
