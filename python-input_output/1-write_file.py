#!/usr/bin/python3


"""
This module contains a function `write_file` that writes a string to a text file.
"""


def write_file(filename, text=""):
    """
    Write a string to a text file.

    Args:
        filename (str): The name of the file to write to.
        text (str, optional): The string to write to the file. Defaults to "".
    """
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
