#!/usr/bin/python3
def uppercase(str):
    cnvrt_str = ""

    for i in range(len(str)):
        if 97 <= ord(str[i]) and ord(str[i]) <= 122:
            cnvrt_char = chr(ord(str[i]) - 32)
            cnvrt_str += cnvrt_char
        else:
            cnvrt_str += str[i]

    print("{:s}".format(cnvrt_str))
