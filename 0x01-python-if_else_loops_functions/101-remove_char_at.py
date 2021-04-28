#!/usr/bin/python3
def remove_char_at(str, n):
    for x in range(len(str)):
        if x == n and x >= 0:
            return(str[:x] + str[x + 1:])
        else:
            return(str)
