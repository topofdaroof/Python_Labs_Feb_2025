#! /usr/bin/env python3
# Author: Name
# Description: This module contains a collection of calculator functions
"""
Basic calculator functions including add, multiple and divide
"""
import sys

def add(*args):
    """ Return SUM of all parameters"""
    total = 0
    for num in args:
        total += num
    return total

def mul(*args):
    """ Return Product """
    total = 1
    for num in args:
        total *= num
    return total

def div(x, z):
    """ Return quotient """
    return round (x/z, 3)

def main():

    print("Basic Calculator App")
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 + 3 + 2 = {add(4, 3, 2)}")
    print(f"4 / 3 = {div(4,3)}")
    return None

# Namespace TRICK
if __name__ == "__main__":
    #executes only when run directly as a program
    main()
    sys.exit(0)


