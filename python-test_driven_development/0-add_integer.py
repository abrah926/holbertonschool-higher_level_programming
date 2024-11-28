#!/usr/bin/python3
"""
Module that defines a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int or float): The first number to add.
    b (int or float, optional): The second number to add, defaults to 98.

    Returns:
    int: The sum of the two numbers, cast to an integer.

    Raises:
    TypeError: If `a` or `b` is not an integer or a float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers
    a = int(a)
    b = int(b)

    return a + b
