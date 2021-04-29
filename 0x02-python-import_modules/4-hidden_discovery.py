#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    argv = dir(hidden_4)
    for argc in range(len(argv)):
        if argv[argc][:2] != '__':
            print("{:s}".format(argv[argc]))
