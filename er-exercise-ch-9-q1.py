#! /usr/bin/env python3
# Author: Name
# Description: This script will generate
"""
Docstring:
"""

def frange(start, stop, step=0.25):
    """ sequence of floats """
    if step == 0:
        raise ValueError("No 0 value can be entered")
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step
