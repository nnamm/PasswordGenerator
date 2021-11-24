import secrets


def create_random_chars(letters: str, length: int) -> str:
    return "".join(secrets.choice(letters) for _ in range(length))
