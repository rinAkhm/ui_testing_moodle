from common.constants import LoginConstants, DataConstants
from models.auth import AuthData
import pytest
import allure
import logging

logger = logging.getLogger("moodle")


class TestAuth:
    @pytest.mark.auth_page
    @allure.title("Test auth with valid data")
    @allure.severity("blocker")
    def test_auth_valid_data(self, app, get_auth_data):
        """
        Steps:
        1. Open main page
        2. Auth with valid login and password
        3. Check auth result
        """
        app.open_main_page()
        app.login.auth(get_auth_data)
        assert app.login.is_auth(), "You are not auth with valid data"

    @pytest.mark.auth_page
    @allure.title("Test auth with invalid data")
    @allure.severity("critical")
    def test_auth_invalid_data(self, app):
        """
        1. Open main page
        2. Auth with invalid login and password
        3. Check auth result
        """
        app.open_main_page()
        app.logger().info("generate invalid data for sign in")
        data = AuthData.generate_data()
        app.login.auth(data)
        assert (
            LoginConstants.MASSAGE_ERROR == app.login.login_error()
        ), "You are auth with invalid data"

    @pytest.mark.auth_page
    @allure.severity("critical")
    @pytest.mark.parametrize("param1, param2", DataConstants.data)
    def test_scope(self, app, param1, param2):
        """
        1. Open main page
        2. Auth with [
            - login and empty password,
            - empty login and password,
            - empty login and empty password]
        3. Check auth result
        """
        app.open_main_page()
        app.logger().info("Used data from parametrize constants")
        data = AuthData(login=param1, password=param2)
        app.login.auth(data)
        assert (
            LoginConstants.MASSAGE_ERROR == app.login.login_error()
        ), "You are auth with empty params"
