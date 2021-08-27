from common.constants import LoginConstants, DataConstants
from models.auth import AuthData
import pytest


class TestAuth:
    def test_auth_valid_data(self, app):
        """
        Steps:
        1. Open main page
        2. Auth with valid login and password
        3. Check auth result
        """
        app.open_main_page()
        data = AuthData(login="rin_akhm@bk.ru", password="Qwerty@321")
        app.login.auth(data)
        assert app.login.is_auth(), "We are not auth"

    def test_auth_invalid_data(self, app):
        """
        1. Open main page
        2. Auth with invalid login and password
        3. Check auth result
        """
        app.open_main_page()
        data = AuthData.generate_data()
        app.login.auth(data)
        assert LoginConstants.MASSAGE_ERROR == app.login.login_error(), "We are auth"

    @pytest.mark.parametrize("param1, param2", DataConstants.data)
    def test_scope(self, app, param1, param2):
        """
        1. Open main page
        2. Auth with [login and empty password,
                      empty login and password,
                      empty login and empty password]
        3. Check auth result
        """
        app.open_main_page()
        data = AuthData(login=param1, password=param2)
        app.login.auth(data)
        assert LoginConstants.MASSAGE_ERROR == app.login.login_error(), "We are auth"
