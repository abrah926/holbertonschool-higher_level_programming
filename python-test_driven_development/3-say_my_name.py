#!/usr/bin/python3
"""Module for say_my_name function."""


def say_my_name(first_name, last_name=""):
    """
    Print all names

    Args:
    first_name: string of first name
    last_name: string of last name

    Return:
    Function that prints a string with first and last name

    Raises:
    TypeError:  if first name is not a string
                if last name is not a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}" .format(first_name, last_name))
