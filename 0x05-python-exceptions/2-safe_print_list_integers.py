#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    nums = 0

    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end="")
            nums += 1
        except (ValueError, TypeError):
            continue
    print()
    return nums
