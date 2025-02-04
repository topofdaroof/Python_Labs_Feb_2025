#! /usr/bin/env python3
# Author: Eul
# Description: This script will demo
"""
Docstring:
"""

#ITERATE through all th echars in the Unicode table
# using an iterator for loop (0 -> 65535

for pos in range(0, 65536):
    try:
        print(chr(pos), end=" ")
        if pos % 16 == 0:
            print()
    except UnicodeError:
        print(" ", end=" ")