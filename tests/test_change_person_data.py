import pytest

from models.auth import AuthData
from models.profile import ProfileData as PD

from pages.application import Application


class TestChangeProfileData:
    """Change data profile."""

    @pytest.mark.profile_data
    def test_change_profile(
        self, app: Application, get_auth_data: AuthData, login_up: None
    ) -> None:
        """
        Steps:
        1. Open main page
        2. auth in moodle
        3. check sign in
        4. generate random data for profile
        5. submit changed data in profile
        6. check save
        """
        assert app.login.is_auth(), "You are not auth"
        data = PD().generate_data_profile()
        app.profile.change_profile_data(data)
        assert (
            "Изменения сохранены" in app.profile.check_valid_changed()
        ), "profile not changed"

    @pytest.mark.profile_data
    @pytest.mark.parametrize(
        "firstname, lastname",
        [
            [None, PD.generate_data_profile().lastname],
            [PD.generate_data_profile().firstname, None],
        ],
    )
    def test_required_field_from_profile_page(
        self, app: Application, firstname: str, lastname: str, login_up: None
    ) -> None:
        """
        Steps:
                1. Open main page
                2. auth in moodle
                3. check sign in
                4. generate random data for profile
                5. submit changed data in profile
                6. check save
        """
        assert app.login.is_auth(), "You are not auth"
        data = PD().generate_data_profile()
        setattr(data, "firstname", firstname)
        setattr(data, "lastname", lastname)
        error_text = app.profile.check_required_fields(data)
        assert "Заполните поле" in error_text, "profile changed"
