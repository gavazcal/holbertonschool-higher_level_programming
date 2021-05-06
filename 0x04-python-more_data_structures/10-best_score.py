#!/usr/bin/python3


def best_score(a_dictionary):
    if (a_dictionary):
        largest = max(a_dictionary.values())
        for key, val in a_dictionary.items():
            if val is largest:
                return key
    else:
        return None
