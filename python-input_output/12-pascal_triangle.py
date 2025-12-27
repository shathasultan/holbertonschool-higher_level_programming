#!/usr/bin/python3
"""
Generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Return a list of lists representing Pascal's triangle of n rows.

    Args:
        n (int): Number of rows.

    Returns:
        list: A list of lists, where each inner list represents a row.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        p_row = triangle[-1]
        row = [1]

        for j in range(1, i):
            row.append(p_row[j - 1] + p_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
