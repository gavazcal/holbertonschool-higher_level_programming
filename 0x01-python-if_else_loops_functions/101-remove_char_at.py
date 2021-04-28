#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = ""
    for x in range(len(str)):
        if x != n:
            str_cpy += str[x]
    return(str_cpy)
