#!/usr/bin/python3
def no_c(my_string):
    cless = ""
    for idx in range(len(my_string)):
        if my_string[idx] != 'C' and my_string[idx] != 'c':
            cless += my_string[idx]
    return cless
