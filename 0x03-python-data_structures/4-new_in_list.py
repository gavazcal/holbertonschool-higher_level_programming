#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_dup = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return list_dup
    else:
        list_dup[idx] = element
    return list_dup
