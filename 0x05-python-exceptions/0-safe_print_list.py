#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    y = 0
    for y in range(0, x):
        try:
            print(my_list[y], end="")
            y += 1
        except:
            break
    print()
    return y
