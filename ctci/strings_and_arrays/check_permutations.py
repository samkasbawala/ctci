from __future__ import annotations
from typing import Dict


def check_permutation(string_1: str, string_2: str) -> bool:
    """Checks if the given strings are a permutation of one another"""

    # Both strings must be of the same size if they are permutations
    # Otherwise, sort and compare
    # O(n log n)
    return (
        False
        if len(string_1) != len(string_2)
        else sorted(string_1) == sorted(string_2)
    )


def check_permutation_freq(string_1: str, string_2: str) -> bool:
    """Checks if the given strings are a permutation of one another"""

    # Both strings must be of the same size if they are permutations
    if len(string_1) != len(string_2):
        return False

    # Store frequencies
    freq: Dict[str, int] = {}

    # Get frequencies
    for char in string_1:
        freq[char] = freq.get(char, 0) + 1

    # Check frequencies of other string
    for char in string_2:

        # If no more letters left or not in freq mapping, return False
        if freq.get(char, 0) < 1:
            return False

        # Char used
        freq[char] -= 1

    # If we make it down here, then return true
    # O(n)
    return True
