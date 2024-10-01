#!/usr/bin/python3


"""
This module contains a function `from_json_string` that returns a Python object
from a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object represented by the JSON string.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        object: The Python object represented by the JSON string.
    """

    return json.loads(my_str)
