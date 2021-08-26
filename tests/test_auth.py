from common.constants import LoginConstants
from models.auth import AuthData


class TestAuth:
    def test_auth_valid_data(self, app):
        """
        Steps:
        1. Open main page
        2. Auth with valid login and password
        3. Check auth result
        """
        app.open_main_page()
        app.login.auth(login="rin_akhm@bk.ru", password="Qwerty@321")
        assert app.login.is_auth(), "We are not auth"
        app.login.log_out()
        assert (
            LoginConstants.MASSAGE_LOGOUT == app.login.check_log_out()
        ), "We are log out system"

    def test_auth_invalid_data(self, app):
        """
        1. Open main page
        2. Auth with invalid login and password
        3. Check auth result
        """
        app.open_main_page()
        data = AuthData.generate_data()
        app.login.auth(login=data.login, password=data.password)
        assert LoginConstants.MASSAGE_ERROR == app.login.login_error(), "We are auth"
