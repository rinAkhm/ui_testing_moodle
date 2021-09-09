from pages.base_page import BasePage

from locators.admin_console import BarLocators
from locators.admin_console import AdminInterfaceLocators


class AddCourse(BasePage):
    """Contain methods for create/delete course."""

    def admin_console(self):
        return self.find_clickable_element(BarLocators.BTN_ADMIN_BAR)

    def category_courses(self):
        return self.find_clickable_element(AdminInterfaceLocators.LINK_COURSES)

    def add_course(self):
        return self.find_clickable_element(AdminInterfaceLocators.LINK_ADD_COURSE)

    def btn_save(self):
        return self.find_clickable_element(AdminInterfaceLocators.BTN_SAVE)

    def input_name_course(self):
        return self.find_element(AdminInterfaceLocators.FULL_NAME_COURSE)

    def input_short_name(self):
        return self.find_element(AdminInterfaceLocators.SHORT_NAME_COURSE)

    def find_course_name(self):
        return self.find_element(AdminInterfaceLocators.CHECK_NEW_COURSE).text

    def admin_page(self):
        return self.find_elements(BarLocators.BTN_ADMIN_BAR)

    def is_admin_page(self):
        """Chek is open admin page."""
        element = self.find_elements(BarLocators.ADMIN_PAGE)
        if len(element) > 0:
            return True
        return False

    def new_course(self, data):
        """create new course."""
        if not self.is_admin_page():
            self.click_element(self.admin_console())
            self.click_element(self.category_courses())
        self.click_element(self.add_course())
        self.app.logger().info(
            f'Add new course name-"{data.full_name}"'
            f'and short name-"{data.short_name}"'
        )
        self.fill_element(self.input_name_course(), data.full_name)
        self.fill_element(self.input_short_name(), data.short_name)
        self.click_element(self.btn_save())

    def delete_course(self):
        return self.find_elements(AdminInterfaceLocators.ICON_DELETE_COURSE)[1]

    def delete_btn(self):
        return self.find_element(AdminInterfaceLocators.BTN_DELETE)

    def was_deleted_course(self):
        return self.find_element(AdminInterfaceLocators.MESSAGE_DELETE).text

    def manager_courses(self):
        return self.find_clickable_element(AdminInterfaceLocators.LINK_MANAGER_COURSE)

    def delete_new_course(self):
        """delete first course in list."""
        if not self.is_admin_page():
            self.click_element(self.admin_console())
            self.click_element(self.category_courses())
        self.click_element(self.manager_courses())
        self.app.logger().info("Delete created course")
        self.click_element(self.delete_course())
        self.click_element(self.delete_btn())
