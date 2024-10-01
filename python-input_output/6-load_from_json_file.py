#!/usr/bin/python3
"""
This module contains a function `load_from_json_file` that creates an object
from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)
