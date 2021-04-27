#!/usr/bin/python3
for i in reversed(range(97, 123)):
    uppercase = (i - 32) - 1
    if i % 2 == 0:
        print("{}{}".format(chr(i), chr(uppercase)), end="")
