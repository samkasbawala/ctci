from __future__ import annotations


def string_rotation(string_1: str, string_2: str) -> bool:
    """Returns a boolean value indicating whether or not string_2 is a rotation of
    string_1.

    Args:
        string_1 (str): string
        string_2 (str): string

    Returns:
        bool: returns whether or nor the strings are a rotatation of one another
    """

    string_2 = string_2 + string_2
    return string_1 in string_2
