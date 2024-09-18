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
        OverflowError: If the result is too large to be represented.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Convert to integer
    a = int(a)
    b = int(b)

    # Perform the addition and handle potential overflow
    result = a + b
    if result == float('inf') or result == float('-inf'):
        raise OverflowError("integer addition overflow")

    return result
