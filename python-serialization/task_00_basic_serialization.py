#!/usr/bin/python3


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the Python dictionary 'data' to a JSON file.

    Parameters:
    - data: The Python dictionary to serialize.
    - filename: The output file to save the serialized data. If it exists, it will be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    Parameters:
    - filename: The input file to load the data from.

    Returns:
    A Python dictionary with the deserialized data.
    """
    with open(filename, 'r') as file:
        return json.load(file)
