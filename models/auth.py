from faker import Faker

fake = Faker("Ru-ru")


class AuthData:
    def __init__(self, login: str = None, password: str = None):
        self.login = login
        self.password = password

    @staticmethod
    def generate_data():
        login = fake.email()
        password = fake.password()
        return AuthData(login, password)
