#!/usr/bin/python3
"""Module to add two integers.

The function `add_integer` takes two numbers and returns their sum after casting
them to integers if necessary. It raises a TypeError if the inputs are not valid.
"""

def add_integer(a, b=98):
    """Add two integers or floats.

    Args:
        a: First number.
        b: Second number (default is 98).

    Returns:
        The sum of `a` and `b` as an integer.

    Raises:
        TypeError: If `a` or `b` are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    try:
        result = add_integer(1e308, 1e308)
    except OverflowError:
        print("Overflow error occurred")

    
    return int(a) + int(b)
