from application import get_fake_name, get_fake_city_name


def get_fake_human() -> str:
    """
    The function returns a random full name and a random city name.
    """
    return f"Hello my name Is {get_fake_name()}, and i live in {get_fake_city_name()}."


if __name__ == "__main__":
    print(get_fake_human())
