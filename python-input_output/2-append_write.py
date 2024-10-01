#!/usr/bin/python3


"""
This module contains a function `append_write`
that appends a string to a file and prints the
number of characters written."""


def append_write(filename="", text=""):
    """
    Append a string to a file and print the number of characters written.

    Args:
        filename (str, optional): The name of the file to append to.
        Defaults to "".
        text (str, optional): The string to append to the file.
        Defaults to "".
    """
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
        print(len(text))
