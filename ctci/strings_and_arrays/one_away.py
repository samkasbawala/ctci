from __future__ import annotations


def one_away(string_1: str, string_2: str) -> bool:
    """Returns a boolean value indicating whether the two strings are one edit away.

    Args:
        string_1 (str): first of the strings to compare
        string_2 (str): second of the strings to compare

    Returns:
        bool: whether the two strings are one edit away
    """

    # Lengths cannot differ my more than 2
    if abs(len(string_1)) - abs(len(string_2)) >= 2:
        return False

    if string_1 == string_2:
        return True

    # Same length, there must be only one spot of difference
    if len(string_1) == len(string_2):
        difference = False
        for ch_1, ch_2 in zip(string_1, string_2):
            if not difference and ch_1 != ch_2:
                difference = True

            elif ch_1 != ch_2:
                return False

    # Differing lengths by one
    else:

        # Identify longer string and shorter string
        long_string = string_1 if len(string_1) > len(string_2) else string_2
        short_string = string_1 if len(string_1) <= len(string_2) else string_2

        long_index = 0
        short_index = 0

        # Have we come across a missing char
        skipped = False

        # If we make it through the while loop, then we know it's one edit away
        while short_index < len(short_string) and long_index < len(long_string):

            # We have not seen one char missing yet, and all chars up until now have
            # matched, increment long_index by one
            if not skipped and short_string[short_index] != long_string[long_index]:
                skipped = True
                long_index += 1

            # Second time we are seeing a missing char, must be false
            elif short_string[short_index] != long_string[long_index]:
                return False

            # Same letter
            else:
                short_index += 1
                long_index += 1

    # If we make it here, then the strings must be one edit away
    return True
