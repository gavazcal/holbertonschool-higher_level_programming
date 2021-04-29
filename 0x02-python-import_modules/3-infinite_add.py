#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    result = 0
    if len(argv) == 0:
        print("0")
    elif len(argv) > 0:
        for x in range(1, len(argv)):
            result += int(argv[x])
        print("{:d}".format(result))
