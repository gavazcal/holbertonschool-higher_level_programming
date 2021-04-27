#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digit = (abs(number) % 10) * -1
if last_digit > 5:
    string = "greater than 5"
elif last_digit == 0:
    string = "0"
else:
    string = "less than 6 and not 0"

print("Last digit of {:d} is {:d} and is {:s}".format(number, last_digit, string))
