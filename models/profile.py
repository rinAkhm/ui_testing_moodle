from faker import Faker
import random
import os

from common.constants import DataConstants

fake = Faker("Ru-ru")


class ProfileData:
    def __init__(
        self,
        firstname: str = None,
        lastname: str = None,
        city: str = None,
        country: str = None,
        timezone: str = None,
        email_mod: str = None,
        moodle_net: str = None,
        image: str = None,
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.country = country
        self.timezone = timezone
        self.email_mod = email_mod
        self.moodle_net = moodle_net
        self.image = image

    @staticmethod
    def generate_data_profile():
        firstname = fake.first_name()
        lastname = fake.last_name()
        city = fake.city()
        country = random.choice(DataConstants.country_list)
        timezone = random.choice(DataConstants.time_zone)
        email_mod = random.choice(DataConstants.email_mod)
        moodle_net = fake.url()
        image = ProfileData()

        return ProfileData(
            firstname,
            lastname,
            city,
            country,
            timezone,
            email_mod,
            moodle_net,
            image.images(),
        )

    def images(self):
        files = random.choice(["image1.jpg", "image2.jpg"])
        image = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            fr"images/{files}",
        )
        return image
