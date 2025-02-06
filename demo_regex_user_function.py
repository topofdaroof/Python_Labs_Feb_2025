#! /usr/bin/env python3
# Author: DCameron
# Description: This script will generate 6 RANDOM lottery numbers.
"""
    Docstring:
"""
import re

# Example of a user function with parameter passing
# and default values
def search_pattern(pattern=r"^.{19}$", file=r"c:\labs\words"):
    lines = 0
    fh_in = open(file, mode="rt")

    for line in fh_in:
        m = re.search(pattern, line)  # Match lines 5 char palindromes
        # m = re.search(r"^([A-Z]).*\1$", line, flags=re.IGNORECASE)  # Match lines start/end with SAME CAPITAL!
        if m:
            lines += 1
            print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")

    return lines


search_pattern()

# Now use the CALLER as a r-val
num_lines = search_pattern(r"^([A-Z]).*\1$", r"c:\labs\words")
print(f"Matched {num_lines} lines")
