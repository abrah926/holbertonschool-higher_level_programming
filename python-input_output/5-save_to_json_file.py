#!/usr/bin/python3
"""
This module contains a function `save_to_json_file` that writes an object to
a text file using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        filename (str): The name of the file to write to.
        obj (object): The object to be written to the file.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
