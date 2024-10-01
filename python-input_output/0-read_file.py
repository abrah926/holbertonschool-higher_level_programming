#!/usr/bin/python3


"""
This module contains a function `read_file` that reads and prints
the content of a UTF-8 encoded text file to stdout.
"""


def read_file(filename=""):
    """_summary_

    Args:
        filename (str, optional): The name of the file to be read. Defaults to "".
    """
    with open(filename, "r", encoding='utf-8') as file:
        print(file.read(), end="")
