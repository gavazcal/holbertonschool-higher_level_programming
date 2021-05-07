#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list == []:
        return 0
    av = 0
    tot = 0
    for a, b in my_list:
        av += a * b
        tot += b
    return (av / tot)
