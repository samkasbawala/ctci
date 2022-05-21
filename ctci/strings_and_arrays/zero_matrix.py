from __future__ import annotations
from typing import Any, List


def zero_matrix(matrix: List[List[Any]]) -> List[List[Any]]:
    """If an element in the matrix is 0, then it sets the entire row and column to 0.

    Args:
        matrix (List[List[Any]]): matrix

    Returns:
        List[List[Any]]: matrix
    """

    n = len(matrix)

    if n <= 0:
        return matrix

    m = len(matrix[0])

    cols = set()
    rows = set()

    # Get all the rows and columns that need to be converted to 0s
    for i in range(n):
        for j in range(m):

            # If 0, note row and column
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # Convert rows
    for i in rows:
        for j in range(m):
            matrix[i][j] = 0

    # Convert cols
    for j in cols:
        for i in range(n):
            matrix[i][j] = 0

    # Return matrix
    return matrix
