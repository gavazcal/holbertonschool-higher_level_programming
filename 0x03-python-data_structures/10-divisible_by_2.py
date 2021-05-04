#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    modulus_check = []
    for x in my_list:
        if x % 2 == 0:
            modulus_check.append(True)
        else:
            modulus_check.append(False)
    return modulus_check
