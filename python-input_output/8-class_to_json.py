#!/usr/bin/python3


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        Dictionary containing all instance variables that can be serialized.
    """
    return obj.__dict__
