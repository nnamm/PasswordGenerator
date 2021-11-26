"""Utilities"""

import secrets


def create_random_chars(letters: str, length: int) -> str:
    """Create random characters based letters.

    Args:
        letters (str): Chars from which it was generated
        length (int): Number of chars.

    Returns:
        Random chars.

    """
    return "".join(secrets.choice(letters) for _ in range(length))
