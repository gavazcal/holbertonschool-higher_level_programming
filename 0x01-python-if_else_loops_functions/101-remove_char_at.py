#!/usr/bin/python3
def remove_char_at(str, n):
    for x in range(len(str)):
        if x == n:
            return(str[:x] + str[x+1:])
        elif n > len(str) or n < 0:
            return(str)
