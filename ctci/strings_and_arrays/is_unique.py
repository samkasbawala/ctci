from __future__ import annotations


def is_unique(string: str) -> bool:
    """Determines whether or not a string has all unique characters"""

    # Strings of this length will always have unique characters
    if len(string) <= 1:
        return True

    # Set to hold chars that we have seen
    chars = set()

    # Loop through chars in string, check to see if we have seen this already
    for char in string:
        if char in chars:
            return False

        chars.add(char)

    # If we get here, then all characters in the string are unique
    return True


def is_unique_no_additional_data_structure(string: str) -> bool:
    """Determines whether or not a string has all unique characters"""

    # Strings of this length will always have unique characters
    if len(string) <= 1:
        return True

    # Check every pair of characters in the string to see if they match
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False

    # If we get here, then all characters in the string are unique
    return True
