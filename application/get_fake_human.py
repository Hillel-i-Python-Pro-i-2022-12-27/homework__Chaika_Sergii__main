from faker import Faker
fake = Faker()


def get_fake_name() -> str:
    """
    This function returns a random male or female first name.
    """
    return fake.name()


def get_fake_city_name() -> str:
    """
    The function returns a random city name.
    """
    return fake.city()
