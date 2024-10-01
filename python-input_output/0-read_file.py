#!/usr/bin/python3


def read_file(filename=""):
    """_summary_

    Args:
        filename (str, optional): The name of the file to be read. Defaults to "".
    """
    with open(filename, "r", encoding='utf-8') as file:
        print(file.read(), end="")
