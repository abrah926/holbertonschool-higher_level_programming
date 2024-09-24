#!/usr/bin/python3
"""
Module for object attribute and method lookup.
Defines a function lookup() to retrieve a list of an object's attributes.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of the object's attributes and methods.
    """
    return dir(obj)

