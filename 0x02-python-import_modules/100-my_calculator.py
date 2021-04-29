#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if (len(argv) != 4):
        print("Usage: ./100-mycalculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    result = 0
    if operator == '+':
        result = add(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
    elif operator == '-':
        result = sub(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
    elif operator == '*':
        result = mul(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
    elif operator == '/':
        result = div(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
