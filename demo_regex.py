#! /usr/bin/env python3
# Author: DCameron
# Description: This script will generate 6 RANDOM lottery numbers.
"""
    Docstring:
"""
import re

# Open File Handle for READING in TEXT mode
fh_in = open(r"c:\labs\words", mode="rt")

# ITERATE through file handle one line at a time.
for line in fh_in:
    # Example of str testing = GOOD!
    # if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    # m = re.search("^the", line) # Match lines starting with 'the'
    # m = re.search("ing$", line)  # Match lines ending with 'ing'
    m = re.search("^ring$", line)  # Match lines ending with 'ing'
    if m:
        print(line, end="")
