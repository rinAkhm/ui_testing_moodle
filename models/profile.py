from faker import Faker

fake = Faker()


class ProfileData:
    def __init__(self, firstname: str = None, lastname: str = None, city: str = None):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city

    @staticmethod
    def generate_data_profile():
        firstname = fake.first_name()
        lastname = fake.last_name()
        city = fake.city()
        return ProfileData(firstname, lastname, city)
