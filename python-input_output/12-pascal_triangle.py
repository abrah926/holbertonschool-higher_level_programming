#!/usr/bin/python3


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = []  # This will hold the rows of the triangle

    for i in range(n):
        row = [1] * (i + 1)  # Start with a row filled with 1s

        # Fill in the internal values based on the previous row
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
