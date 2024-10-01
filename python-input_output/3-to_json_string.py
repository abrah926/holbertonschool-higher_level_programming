#!/usr/bin/python3
"""
This module contains a function `to_json_string` that returns the JSON
representation of an object (string).
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        obj (object): The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
