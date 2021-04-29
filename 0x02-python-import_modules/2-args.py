#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg_count = len(argv) - 1
    if arg_count == 0:
        print("{} arguments.".format(arg_count))
    elif arg_count == 1:
        print("{} argument:".format(arg_count))
        print("{}: {}".format(arg_count, argv[arg_count]))
    elif arg_count > 1:
        print("{} arguments:".format(arg_count))
        for x in range(1, arg_count + 1):
            print("{:d}: {}".format(x, argv[x]))
