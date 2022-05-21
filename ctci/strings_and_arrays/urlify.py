from __future__ import annotations
from typing import List


def urlify(string: List[str], length: int) -> List[str]:
    """Replaces all the spaces in an string with %20

    Args:
        string (List[str]): list representation of the string
        length (int): true length of the string

    Returns:
        str: returns a url-ified string
    """

    # Start from the end of the string array
    cur_length = 0
    insert_point = len(string) - 1
    current_letter_point = len(string) - 1

    while current_letter_point > 0:

        # Haven't seen a letter yet
        if cur_length == 0 and string[current_letter_point] == " ":
            current_letter_point -= 1

        # At a char
        elif string[current_letter_point] != " ":
            string[insert_point] = string[current_letter_point]
            insert_point -= 1
            current_letter_point -= 1
            cur_length += 1

        # At a space
        else:
            string[insert_point] = "0"
            string[insert_point - 1] = "2"
            string[insert_point - 2] = "%"

            insert_point -= 3
            current_letter_point -= 1
            cur_length += 1

    return string


if __name__ == "__main__":
    print(
        urlify(
            [
                "M",
                "r",
                " ",
                "J",
                "o",
                "h",
                "n",
                " ",
                "S",
                "m",
                "i",
                "t",
                "h",
                " ",
                " ",
                " ",
                " ",
            ],
            13,
        )
    )
