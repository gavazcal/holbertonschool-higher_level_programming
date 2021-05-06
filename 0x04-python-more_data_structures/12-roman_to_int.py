#!/usr/bin/python3


def roman_to_int(roman_string):
    r = 0
    s = roman_string
    cnv = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    if type(roman_string) != str or len(roman_string) == 0:
        return 0
    else:
        for i in range(len(roman_string)):
            if i < len(s) - 1:
                r += cnv[s[i]] if cnv[s[i]] >= cnv[s[i + 1]] else cnv[s[i]] * -1
            else:
                r += cnv[s[i]]
        return r
