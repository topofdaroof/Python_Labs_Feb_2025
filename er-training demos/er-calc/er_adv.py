#! /usr/bin/env python3
# Author: Name
# Description: This module contains a collection of calculator functions
"""
Basic calculator functions including add, multiple and divide
"""

import sys


def mod (x, z):
    """ Return remainder of x divided by z """
    return x % z

def power (x, z):
    """ Return POWER of x to z """
    return x**z

def sqrt (x, z):
    """ Return sqrt x """
    return round(x**0.5, 2)

print("ADVANCED Clac App")
print("-"*30)

print(f"100 % 30 = {mod(100, 30)}")
print(f"100 ** 3= {power(100,3)}")
print(f"100 ** 3= {sqrt(100,3)}")


