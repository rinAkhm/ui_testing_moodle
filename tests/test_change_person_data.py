from models.auth import AuthData
from models.profile import ProfileData


class TestChangeProfileData:
    """Change data profile."""

    def test_change_profile(self, app):
        """
        Steps:
        1. Open main page
        2. auth in moodle
        3. check sign in
        4. generate random data [firstname, lastname, city]
        5. change profile
        6. check save
        """
        app.open_main_page()
        if not app.login.is_auth():
            data = AuthData(login="rin_akhm@bk.ru", password="Qwerty@321")
            app.login.auth(data)
            assert app.login.is_auth(), "You are not auth"
        data = ProfileData().generate_data_profile()
        app.profile.change_profile_data(data.firstname, data.lastname, data.city)
        assert (
            "Изменения сохранены" in app.profile.check_valid_changed()
        ), "profile not changed"
