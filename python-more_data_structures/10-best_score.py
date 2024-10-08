#!/usr/bin/python3


def best_score(a_dictionary):

    if not a_dictionary:
        return None
    
    best_key = None
    max_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > max_value:
            best_key = key
            max_value = value

    return best_key