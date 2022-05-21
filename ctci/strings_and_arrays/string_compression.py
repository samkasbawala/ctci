from __future__ import annotations


def string_compression(string: str) -> str:
    """Returns a compressed version of the inputted string. If the compressed string is
    longer than original string, then the original string is returned.

    Args:
        string (str): input string

    Returns:
        str: compressed string
    """

    # No compression needed on a string this short
    if len(string) < 2:
        return string

    # Use list to hold string, then appending to string becomes a constant operation
    new_string_list = []

    # Times we have seen the prev char
    count = 1

    # Loop through remaining chars
    for index in range(1, len(string)):

        # If the prev char and the current char match, increment count
        if string[index - 1] == string[index]:
            count += 1

        # Otherwise, extend new string with char and count, reset count
        else:
            new_string_list.extend([string[index - 1], str(count)])
            count = 1

    # Make sure to add the last char and count
    new_string_list.extend([string[-1], str(count)])

    # Create an actual str object out of the string list
    new_string = "".join(new_string_list)

    return string if len(string) <= len(new_string) else new_string
