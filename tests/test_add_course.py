import allure
import pytest

from models.add_course import CourseData
from pages.application import Application


class TestAddCourse:
    """Contain tests create and delete course."""

    @pytest.mark.add_course
    @allure.title("Create new course")
    def test_add_course(self, app: Application, login_up: None) -> None:
        """
        Steps:
        1. Login in system
        2. Open admin bar
        3. Open course category
        4. Add new course
        4. Check to added
        """
        assert app.login.is_auth(), "You are not auth"
        data = CourseData().generate_data()
        app.course.new_course(data)
        assert (
            app.course.find_course_name() == f"{data.full_name}"
        ), "Course not created"

    @pytest.mark.add_course
    @allure.title("Delete course")
    def test_delete_course(self, app: Application, login_up: None) -> None:
        """
        Steps:
        1. Login in system
        2. Open admin bar
        3. Open page manger courses
        4. Delete first course
        5. Check to deleted
        """
        assert app.login.is_auth(), "You are not auth"
        app.course.delete_new_course()
        assert (
            "был полностью удален" in app.course.was_deleted_course()
        ), "Course not deleted"
