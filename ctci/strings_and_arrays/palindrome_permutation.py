from __future__ import annotations
from typing import Dict


def palindrome_permutation(string: str) -> bool:
    """Returns a boolean indicating whether or not a permutation of the string is a
    palindrome.

    Args:
        string (str): input string

    Returns:
        bool: if a permutation of a string is a palindrome
    """

    # No disticintion made between capital and lowercase characters
    string = string.lower()

    # If length less than 2, true
    if len(string) < 2:
        return True

    # Build a frequency mapping for each char, do not need to account for white space
    freq: Dict[str, int] = {}
    for char in string:
        if char == " ":
            continue
        freq[char] = freq.get(char, 0) + 1

    # Get the number of alphanumeric values in the string
    num_chars = sum(freq.values())

    # Even case, all char frequencies must occur an even number of times
    if num_chars % 2 == 0:
        for value in freq.values():
            if value % 2 != 0:
                return False

    # Odd case, one char must have an odd freq, rest must be even
    else:
        seen_odd = False
        for value in freq.values():

            # Not seen an odd freq yet
            if not seen_odd and value % 2 == 1:
                seen_odd = True

            # Odd freq, but we have already seen another one
            elif value % 2 == 1:
                return False

            # Even freq
            else:
                continue

        # Must have one char that occurs an odd number of times
        if not seen_odd:
            return False

    # If we make it down here, then the string has a permutation that is a palindrome
    return True
