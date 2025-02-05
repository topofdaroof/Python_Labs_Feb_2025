#! /usr/bin/env python3
# Author: Name
# Description: This script will generate
"""
Docstring:
"""
import re
#Open file handle for READING in TEXT mode
fh_in = open(r"c:\labs\words", mode ="rt")
#ITERATE through file hanlde one line at a time
for line in fh_in:
    #if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    # m = re.search("^the", line)
    # m = re.search(r"^[adr]ing$",line) # begin and end with the same capital
    m = re.search(r"^([A-Z]).*\1$", line)
    # m = re.search("[aeiou][aeio]", line)
    # m = re.search("[.]", line)
    # m=re.search("^(.)(.).\2\1$", line)
    if m:
        print(line, end="")