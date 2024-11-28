#!/usr/bin/python3
"""Module for print_square function"""


def print_square(size):
    """
    Print square with the character #.

    Args:
    size: is the size of length of the square

    Returns:
    Print square

    Raises:
    TypeError:  if size < 0
                if size is not an integer

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
