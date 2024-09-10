#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    # Check if the index is out of range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Create a new list excluding the item at the specified index
    new_list = [item for i, item in enumerate(my_list) if i != idx]

    return new_list
