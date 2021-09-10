from faker import Faker

fake = Faker()


class CourseData:
    def __init__(self, full_name: str = None, short_name: str = None):
        self.full_name = full_name
        self.short_name = short_name

    @staticmethod
    def generate_data():
        full_name = fake.job()
        short_name = f"index_{full_name}"
        return CourseData(full_name, short_name)
