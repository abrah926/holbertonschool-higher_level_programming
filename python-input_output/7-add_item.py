#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list
and saves them to a JSON file named add_item.json.
"""

import sys
import importlib
load_from_json_file = importlib.import_module(
    '6-load_from_json_file').load_from_json_file
save_to_json_file = importlib.import_module(
    '5-save_to_json_file').save_to_json_file

filename = 'add_item.json'

try:

    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
